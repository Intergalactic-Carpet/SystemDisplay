from psutil import cpu_percent
import os
cpu_stat = 0
script_dir = os.path.dirname(os.path.abspath(__file__))
base_file = os.path.join(script_dir, 'cpu bridge.txt')
debug = False


def write_file(in_, file_='cpu bridge.txt'):
    with open(file_, 'w') as file:
        file.write(str(in_))
        file.close()


def read_file(in_):
    with open(in_, 'r') as file:
        data = file.readlines()
        file.close()
    if debug:
        print(data[0][0])
    return data


def run():
    global cpu_stat
    write_file(0)
    while True:
        cpu_stat = cpu_percent(0.5, False)
        write_file(cpu_stat)
        if debug:
            print(cpu_stat)
        if read_file(os.path.join(script_dir, 'cpu_stop.txt'))[0][0] == '1':
            break
    write_file(0)
    write_file(0, os.path.join(script_dir, 'cpu_stop.txt'))


run()
