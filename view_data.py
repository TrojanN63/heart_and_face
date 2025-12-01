import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'data.csv'
data = pd.read_csv(file)

def get_rows():
    with open(file) as f:
        return sum(1 for line in f)

def calc_avg():
    Sum = 0
    for i in range(get_rows() - 1):
        Sum += float(data['ypos'][i])
    return Sum/(get_rows()-1)

def show_time():
    for i in range(get_rows()-1):
        print(data['time'][i])

def show_ypos():
    for i in range(get_rows()-1):
        print(data['ypos'][i])

def find_peak():
    response = ''
    for i in range(get_rows() -1):
        if data['ypos'][i] < calc_avg():
            response += f'{data["time"][i]}\n'
    return response

def get_freq(start, end, var, avg):
    if start==-1:
        start = float(data['time'][0])
    if end==-1:
        end = float(data['time'][get_rows()-2])
    if avg==-1:
        avg = calc_avg()
    rev = 0
    for i in range(get_rows()-1):
        time = float(data['time'][i])
        ypos = float(data['ypos'][i])
        if time >= start and time <= end and ypos<(avg-var):
            rev+=1
    rps = rev / (end - start)
    return rps

def show_data():
    nums = []
    for i in data['ypos']:
        nums.append(float(i))
    
    plt.plot(nums, ls='solid')
    plt.show()

def plot_h():
    nums = []
    for i in data['horizontal_pos']:
        nums.append(float(i))

    plt.plot(nums, ls='solid')
    plt.show()

def plot_v():
    nums = []
    for i in data['vertical_pos']:
        nums.append(float(i))

    plt.plot(nums, ls='solid')
    plt.show()
