import pandas as pd

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

def get_freq(start, end, var):
    if start==-1:
        start = float(data['time'][0])
    if end==-1:
        end = float(data['time'][get_rows()-2])
    rev = 0
    for i in range(get_rows()-1):
        time = float(data['time'][i])
        ypos = float(data['ypos'][i])
        if time >= start and time <= end and ypos<(calc_avg()-var):
            rev+=1
    rps = rev / (end - start)
    return rps

print(f'Avarage: {calc_avg()}')
print(f'''List of every time ypos was bellow avarage:
{find_peak()}''')
print(f'Relovutions per second: {get_freq(-1,-1, 0.001)}')
