import datetime
import time


def read_file_to_list(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    return [line.strip() for line in content]


with open('current_time.txt', 'r') as f:
    past_time_str = f.read().strip()

past_time = datetime.datetime.strptime(past_time_str, '%Y-%m-%d %H:%M:%S')

timer_path = "timer.txt"
time_minutes = read_file_to_list(timer_path)

current_time = datetime.datetime.now()
new_time = past_time + datetime.timedelta(minutes=float(timer_path))

if new_time > current_time:
    with open('host.txt', 'w') as input_file:
        input_contents = input_file.read()

    with open(r"/private/etc/hosts", 'r') as output_file:
        output_file.write(input_contents)
    print("time is up, websites unblocked, enjoy")
    time.sleep(5)
else:
    print("keep waiting, your time isn't up yet. Go do ur work stephen.")
    time.sleep(5)
