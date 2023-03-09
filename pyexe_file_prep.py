import os
script_dir = os.path.dirname(os.path.abspath(__file__))


def check_saves():

    with open(os.path.join(script_dir, 'cpu_stop.txt'), 'w') as file:
        file.write('0')
        file.close()

    with open(os.path.join(script_dir, 'cpu bridge.txt'), 'w') as file:
        file.write('0')
        file.close()


check_saves()
