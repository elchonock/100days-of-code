import time
import datetime
# from tkinter import *


class Stopwatch:
    def __init__(self):
        self.start_time = 0
        # self.state_button = 'normal'
        # self.saved = []


    # def state_but(self):
    #     self.state_button = 'disabled'
    #     return self.state_button


    def start(self):
        self.start_time = time.time()

        # ----- попробуй генератор
        # while True:
        #     yield time.time() - self.start_time + 1
        #     time.sleep(1)
        #     self.start_time += 1
    #     ------


    def stop(self):
        time_counter = time.time() - self.start_time
        # self.state_button = 'disabled'
        # self.saved.append(time_counter)


    def reset(self):
        self.start_time = 0


    def display_time(self):
        time_counter = time.time() - self.start_time
        display = round(time_counter)
        return display
        # return str(datetime.timedelta(display))





    # def counter(self):
    #     while 1:
    #         time_flow = self.start_time
    #         time.sleep(1)
    #         self.start_time += 1
    #         return time_flow



#
