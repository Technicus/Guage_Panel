import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Process
import time
import csv
import random
import numpy as np


def realtime_plot():
     # Choose style.
    plt.style.use('fivethirtyeight')
    plt.rcParams['toolbar'] = 'None'

    def animate(i):
        data = pd.read_csv('data.csv')
        x_time = data['x_time']
        y_speed = data['y_speed']
        y_rpm = data['y_rpm']
        gear = data['gear']

        # Clear axes
        plt.cla()
        plt.legend(loc='upper left')
        plt.tight_layout()

        # Overlay subplots
        plt.plot(x_time, y_speed, label='y_speed', linewidth=1)
        plt.plot(x_time, y_rpm, label='y_rpm', linewidth=1)

    animation = FuncAnimation(plt.gcf(), animate, interval=2,cache_frame_data=False)
    plt.tight_layout()
    plt.show()


def data_generator():
     x_time = 0
     y_speed = 0
     y_rpm = 0
     gear = 1

     fieldnames = ["x_time", "y_speed", "y_rpm", "gear"]

     with open('data.csv', 'w') as csv_file:
         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
         csv_writer.writeheader()

     while True:
         with open('data.csv', 'a') as csv_file:
             csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
             info = {
                 "x_time": x_time,
                 "y_speed": y_speed,
                 "y_rpm": y_rpm,
                 "gear": gear
                 }

             csv_writer.writerow(info)
             print(x_time, y_speed, y_rpm, gear)

             x_time += 1

             y_speed = y_speed + random.randint(-5, 5)
             if y_speed < 0:
                 y_speed = 0
             if y_speed > 80:
                 y_speed = 80

             y_rpm = y_rpm + random.randint(-5, 5)
             if y_rpm < 0:
                 y_rpm = 0
             if y_rpm > 80:
                 y_rpm = 80

             if y_rpm  > y_speed :
                 gear = 2
             else:
                 gear =1

             time.sleep(0.025)


data_csv = Process(target=data_generator, args=[])
data_plot = Process(target=realtime_plot, args=[])

if __name__ == '__main__':
    print("start")
    data_csv.start()
    data_plot.start()
    data_csv.join()
    data_plot.join()
    print("end")

