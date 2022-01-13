import threading
import Queue as queue
import serial
from time import sleep
import math
import constant
import os
from helper import Event, debug


class DriverSerial:
    def __init__(self):
        # define

        # run event
        self.run_event = Event()
        self.serial_port = None
        #try:
        self.serial_port = serial.Serial(constant.SERIAL_PORT, constant.SERIAL_BAUD, timeout=0)
        self.run_event.set()
        #except:
        #    debug("[ERROR] SERIAL NOT WORKING. PORT: %s, BAUD: %d" % (constant.SERIAL_PORT, constant.SERIAL_BAUD))
        #    pass
        # callback
        self.callback_data = None
        # data
        self.q = queue.Queue()
        self.checksum = ""
        self.data = ""
        self.state = "IDLE"
        #
        self.queue_serial = queue.Queue()
        # thread
        self.thread_serial = None
        self.thread_serial_send = None
        self.thread_handle_frame = None

    # convert data
    def convert_fire(self, value):
        if value >= 100.0:
            return 1
        return 0

    def convert_temperature(self, value):
        RT0 = 10000.0
        B = 3977.0
        VCC = constant.DC_SOURCE / 1000.0
        R = 10000.0
        T0 = 25 + 273.15
        VRT = value
        VRT = (VCC / constant.COUNT_ADC) * VRT
        VR = VCC - VRT
        RT = VRT / (VR / R)
        if RT == 0:
            return 0
        ln = math.log(RT / RT0)
        TX = (1 / ((ln / B) + (1 / T0))) - 273.15

        return round(TX, 1)

    def convert_current(self, value):
        if value == 0:
            return 0
        return (float(value) * constant.DC_SOURCE / constant.COUNT_ADC - 2500) * 0.0162

    def convert_voltage(self, value):
        if value == 0:
            return 0
        return round((value / constant.COUNT_ADC) * (constant.DC_SOURCE / 1000.0) / (1 - 1.1 / 1.2), 2)

    # callback
    def set_callback_data(self, callback):
        self.callback_data = callback

    # Buffer
    def push(self, ch):
        self.q.put(ch)

    def get_data(self):
        if self.q.empty():
            return

        if self.state == "END_FRAME":
            return

        ch = self.q.get()

        if ch == "$":
            if self.state != "IDLE":
                return
            self.state = "RECEIVING_FRAME"
            self.data = ""
            return

        if ch == "*":
            if self.state != "RECEIVING_FRAME":
                return
            self.state = "RECEIVING_CHECKSUM"
            self.checksum = ""
            return

        if self.state == "RECEIVING_FRAME":
            self.data += ch
            if len(self.data) > 400:
                self.state = "IDLE"
            return

        if self.state == "RECEIVING_CHECKSUM":
            self.checksum += ch

            if len(self.checksum) >= 2:
                self.state = "END_FRAME"
            return

    def handle_frame(self):
        while self.run_event.is_set():
            sleep(0.01)
            if self.state == "END_FRAME":
                raw_data = self.data
                raw_checksum = self.checksum
                self.data = ""
                self.checksum = ""
                self.state = "IDLE"
                try:
                    checksum = 0
                    for ch in raw_data:
                        checksum ^= ord(ch)
                    checksum ^= ord("$")
                    checksum = hex(checksum)[2::]
                    if len(checksum) == 1:
                        checksum = "0" + checksum

                    if checksum != raw_checksum:
                        print "Invalid checksum %s != %s" % (checksum, raw_checksum)
                        continue

                    data = raw_data.split(",")

                    print data

                    if len(data) != 21:
                        print "Invalid data. Length != 21"
                        continue

                    current_item = range(0, 13)

                    voltage = self.convert_voltage(float(data[0 + 1]))

                    for i in range(0, 13):
                        current_item[i] = self.convert_current(float(data[i + 2]))

                    fire = self.convert_fire(float(data[13 + 2]))
                    temperature = self.convert_temperature(float(data[14 + 2]))
                    door = int(float(data[15 + 2]))
                    water = int(float(data[16 + 2]))

                    data = {
                        "voltage": voltage,
                        "current_item": current_item,
                        "temperature": temperature,
                        "fire": fire,
                        "door": door,
                        "water": water
                    }

                    print data

                    if self.callback_data:
                        self.callback_data(data)
                except ValueError:
                    print ValueError

    # Serial action
    def send(self, data):
        if self.serial_port:
            self.queue_serial.put(data)

    def read_from_port(self):
        while self.run_event.is_set():
            sleep(0.001)
            self.get_data()
            reading = self.serial_port.readline().decode()
            if reading:
                for i in reading:
                    self.push(i)

    def send_to_port(self):
        while self.run_event.is_set():
            sleep(0.01)
            if self.queue_serial.empty():
                continue
            data = self.queue_serial.get()
            self.serial_port.write(data.encode())

    def stop(self):
        debug("\r\n*******STOP DRIVER*******\r\n")
        self.run_event.clear()

    def run(self):
        self.thread_handle_frame = threading.Thread(target=self.handle_frame)
        self.thread_handle_frame.start()

        self.thread_serial = threading.Thread(target=self.read_from_port)
        self.thread_serial.start()

        self.thread_serial_send = threading.Thread(target=self.send_to_port)
        self.thread_serial_send.start()


def control_led(status_led):
    #pass
     for led in range(0, 3):
         if led + 1 == status_led:
             os.system("echo -wdout" + constant.PIN_LED[led] + " 1 > /sys/devices/virtual/misc/mtgpio/pin")
         else:
             os.system("echo -wdout" + constant.PIN_LED[led] + " 0 > /sys/devices/virtual/misc/mtgpio/pin")
