from datetime import datetime


def debug(s):
    print datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " -> " + str(s)


def array_zeros(length):
    arr = range(0, length)
    for i in range(0, length):
        arr[i] = 0
    return arr


class Event:
    def __init__(self):
        self.status = False

    def is_set(self):
        return self.status

    def set(self):
        self.status = True

    def clear(self):
        self.status = False
