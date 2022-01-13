# -*- coding: utf-8 -*-

import threading
import requests
import json
from datetime import datetime
import time
import sys
import driver
from helper import debug, array_zeros, Event
import constant
from station_sql import StationSQL
import sync_service

print constant.LOGO_TEXT


class Station:

    def __init__(self):
        sync_config = sync_service.get_station_config()
        self.NUM_CURRENT_METER = sync_config["NUM_CURRENT_METER"]
        #
        self.sql = StationSQL()
        self.sql.connect()
        self.sql.init_table_station_info()
        station_info = self.sql.get_station_info()

        #
        self.station_code = constant.STATION_CODE
        self.SOH_item = array_zeros(self.NUM_CURRENT_METER)
        self.SOH = 100
        self.charge_circle = 0
        self.LLVD = sync_config["LLVD"]
        self.HHTT = sync_config["HHTT"]
        #
        self.SOC = 0
        self.current_item = array_zeros(self.NUM_CURRENT_METER)
        self.current = 0
        self.voltage = 0
        self.temperature = 0
        self.fire = 0
        self.water = 0
        self.door = 0
        #
        self.state = constant.BAT_OFF
        self.last_state = constant.BAT_OFF
        #
        self.flag_calc_soh = 0
        self.temp_wattage = array_zeros(self.NUM_CURRENT_METER)
        #
        self.status_llvd = 0
        self.status_hhtt = 0
        self.status_led = 1
        #
        self.run_event = Event()
        self.run_event.set()
        #
        self.thread_send_data_to_server = None
        self.thread_log_data = None
        self.thread_take_sample_soh = None
        self.thread_save_calc_soh = None
        self.thread_send_serial = None

    # method as service to update data
    def update_data(self, data):
        for key in data:
            setattr(self, key, data[key])

    def template_task(self, timer, target):
        count = 0
        while self.run_event.is_set():
            time.sleep(1)
            count += 1
            if count < timer:
                continue
            count = 0
            target()

    def task_send_data_to_server(self):
        def wrapper():
            # DEBUG
            debug("[INFO] TASK SEND DATA TO SERVER")
            # END DEBUG
            data = [self.station_code]
            data_battery = []
            for i in range(0, self.NUM_CURRENT_METER):
                data_battery.append(
                    [round(self.voltage,1), self.SOH_item[i], round(self.SOC, 1), self.current_item[i]]
                )
            data.append(data_battery)
            data.append(self.charge_circle)
            data.append(round(self.temperature, 1))  # 1
            data.append(round(self.temperature, 1))  # 2
            data.append(round(self.voltage, 1))
            data.append(round(self.current, 1))
            data.append(round(self.SOC, 1))
            data.append(round(self.SOH, 1))
            data.append(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            data = {
                "data": data
            }

            data = json.dumps(data)

            # DEBUG
            debug(data)
            # END DEBUG
            x = requests.post(constant.URL, data, headers=constant.HEADER)
            # DEBUG
            debug(x)
            debug("[INFO] END TASK SEND DATA TO SERVER")
            # END DEBUG

        self.template_task(constant.TIMER_SEND_DATA_TO_SERVER, target=wrapper)

    def task_log_data(self):
        def wrapper():
            debug("[INFO] TASK LOG DATA TO LOCAL")
            # END DEBUG
            data = {
                "current_item": self.current_item,
                "voltage": self.voltage,
                "temperature": self.temperature
            }
            debug(data)
            #
            self.sql.log_data(data)
            #
            debug("[INFO] END TASK LOG DATA TO LOCAL")

        self.template_task(constant.TIMER_LOG_DATA, target=wrapper)

    def task_take_sample_soh(self):
        def wrapper():
            if self.flag_calc_soh:
                debug("[INFO] TASK TAKE SAMPLE SOH")
                for i in range(0, self.NUM_CURRENT_METER):
                    self.temp_wattage[i] += self.voltage * self.current_item[i]
                debug("[INFO] END TASK TAKE SAMPLE SOH")

        self.template_task(constant.TIMER_TAKE_SAMPLE_SOH, target=wrapper)

    def task_save_calc_soh(self):
        def wrapper():
            if self.flag_calc_soh:
                # DEBUG SOH
                debug("SAVE SOH")
                # END DEBUG
                self.sql.log_calc_soh(self.temp_wattage)
                self.temp_wattage = array_zeros(self.NUM_CURRENT_METER)

        self.template_task(constant.TIMER_SAVE_SOH, target=wrapper)

    def task_send_serial(self):
        def wrapper():
            #
            debug("[INFO] TASK SEND SERIAL")
            #

            data1 = [self.voltage, self.current, self.SOC, self.SOH, self.temperature, self.fire, self.water, self.door]

            data2 = [self.NUM_CURRENT_METER]
            for i in range(0, self.NUM_CURRENT_METER):
                data2.append(self.current_item[i])
            for i in range(0, self.NUM_CURRENT_METER):
                data2.append(self.SOH_item[i])

            def get_str_data(code, arr):
                str_data = "$" + code
                for item in arr:
                    str_data += "," + str(round(item, 1))
                checksum = 0
                for ch in str_data:
                    checksum ^= ord(ch)
                checksum = hex(checksum)[2::]
                if len(checksum) == 1:
                    checksum = "0" + checksum
                str_data = str_data + "*" + str(checksum)

                return str_data

            str_data1 = get_str_data("dat1", data1)
            str_data2 = get_str_data("dat2", data2)

            debug(str_data1)
            debug(str_data2)

            driver_serial.send(str_data1)
            driver_serial.send(str_data2)

            debug("[INFO] END TASK SEND SERIAL")

        self.template_task(constant.TIMER_SEND_SERIAL, target=wrapper)

    def push_notify(self, type_notify):
        # DEBUG
        debug("[INFO] PUSH NOTIFY")
        # END DEBUG

        data = {
            "code": self.station_code,
            "status": type_notify,
            "h": 0
        }

        if type_notify == 1:
            remain = 0
            if self.current != 0:
                remain = self.NUM_CURRENT_METER * 10.0 * (self.SOH / 100.0) * (self.SOC / 100.0) / self.current
            data["h"] = remain
        data = json.dumps(data)

        # DEBUG
        debug(data)
        # END DEBUG

        x = requests.post(constant.URL, data, headers=constant.HEADER)

        # DEBUG
        debug(x)
        # END DEBUG
        debug("[INFO] END PUSH NOTIFY")

    def refresh_station(self):
        def calc_soc():
            if self.voltage < 41:
                self.SOC = 0
            else:
                self.SOC = (self.voltage - 41) / 9 * 100
            if self.SOC > 100:
                self.SOC = 100

        def calc_state():
            if self.voltage > 50:
                if self.current < -0.5:
                    self.state = constant.CHARGE
                elif self.current > 0.5:
                    self.state = constant.DISCHARGE
                else:
                    self.state = constant.FULL
            elif self.voltage <= 41:
                self.state = constant.BAT_OFF
            else:
                if self.current > 0.5:
                    self.state = constant.DISCHARGE
                else:
                    self.state = constant.NO_LOAD

        def calc_summary_current():
            if len(self.current_item) == 0:
                self.current = 0
            else:
                self.current = sum(self.current_item) / len(self.current_item)

        def re_update_dry_contact():
            if self.voltage < self.LLVD:
                if self.status_llvd == 0:
                    self.status_llvd = 1
                    debug("[INFO] RELAY LLVD: ON")
                    driver_serial.send("$code,bat1*43")
            else:
                if self.status_llvd == 1:
                    self.status_llvd = 0
                    debug("[INFO] RELAY LLVD: OFF")
                    driver_serial.send("$code,tat1*56")

            if self.temperature > self.HHTT:
                if self.status_hhtt == 0:
                    self.status_hhtt = 1
                    debug("[INFO] RELAY HHTT: ON")
                    driver_serial.send("$code,bat2*40")
            else:
                if self.status_hhtt == 1:
                    self.status_hhtt = 0
                    debug("[INFO] RELAY HHTT: OFF")
                    driver_serial.send("$code,tat2*56")

        def re_update_led_status():
            status_led = 1
            if self.SOC >= 0:
                status_led = 3
            if self.SOC >= 50:
                status_led = 2
            if self.SOC >= 75:
                status_led = 1

            if status_led != self.status_led:
                driver.control_led(status_led)
                self.status_led = status_led

        calc_summary_current()
        calc_soc()
        calc_state()
        re_update_dry_contact()
        re_update_led_status()

        # if self.state == constant.FULL or self.state == constant.BAT_OFF or self.state == constant.NO_LOAD:
        #     for i in range(0, self.NUM_CURRENT_METER):
        #         self.current_item[i] = 0

        # Check state to handle
        if self.state != self.last_state:
            debug("[INFO] STATE CHANGE: %s to %s" % (self.last_state, self.state))
            # Check SOH
            if self.last_state == constant.FULL and (
                    self.state == constant.DISCHARGE or self.state == constant.NO_LOAD):
                # Mat dien
                self.sql.init_table_calc_soh()
                # Run task timer
                self.flag_calc_soh = 1
                self.temp_wattage = array_zeros(self.NUM_CURRENT_METER)
                # DEBUG
                debug("[INFO] TASK CALC SOH RUNNING")
                # END DEBUG
            elif (self.last_state == constant.DISCHARGE or self.last_state == constant.NO_LOAD) and (
                    self.state != constant.BAT_OFF and self.state != constant.DISCHARGE and self.state != constant.NO_LOAD):
                # Co dien
                self.sql.drop_table_calc_soh()
                self.flag_calc_soh = 0
                self.temp_wattage = array_zeros(self.NUM_CURRENT_METER)
                debug("[INFO] TASK CALC SOH STOPPING")
                # END DEBUG
            else:
                pass

            # Check notify
            if self.last_state == constant.CHARGE or self.last_state == constant.FULL:
                if self.state == constant.DISCHARGE or self.state == constant.NO_LOAD:
                    self.push_notify(1)
            elif self.last_state == constant.DISCHARGE or self.last_state == constant.NO_LOAD:
                if self.state == constant.FULL or self.state == constant.CHARGE:
                    self.push_notify(0)
            else:
                pass

            # Update last_state
            self.last_state = self.state

    def run(self):
        driver_serial.run()
        driver.control_led(1)

        self.thread_send_data_to_server = threading.Thread(target=self.task_send_data_to_server)
        self.thread_log_data = threading.Thread(target=self.task_log_data)
        self.thread_take_sample_soh = threading.Thread(target=self.task_take_sample_soh)
        self.thread_save_calc_soh = threading.Thread(target=self.task_save_calc_soh)
        self.thread_send_serial = threading.Thread(target=self.task_send_serial)

        self.thread_send_data_to_server.start()
        self.thread_log_data.start()
        self.thread_take_sample_soh.start()
        self.thread_save_calc_soh.start()
        self.thread_send_serial.start()

        try:
            while self.run_event.is_set():
                time.sleep(0.01)
                self.refresh_station()
        except KeyboardInterrupt:
            debug("[EXCEPT] KEYBOARD INTERRUPT")
            self.run_event.clear()
            driver_serial.stop()
            debug("[EXCEPT] STOP APPLICATION")
            sys.exit()


def callback_data(data):
    station.update_data(data)


station = Station()
driver_serial = driver.DriverSerial()
driver_serial.set_callback_data(callback_data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    station.run()
