import datetime


def write_list_to_file(file_path, content):
    with open(file_path, "w") as file:
        for line in content:
            file.write(line + "")


def read_file_to_list(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    return [line.strip() for line in content]


current_time = datetime.datetime.now()

current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

with open('current_time.txt', 'w') as f:
    f.write(current_time_str)

with open(r"/private/etc/hosts", 'r') as input_file:
    input_contents = input_file.read()

with open('host.txt', 'w') as output_file:
    output_file.write(input_contents)

blocked_path = "blocked_sites.txt"
blocked_websites = read_file_to_list(blocked_path)
hosts_path = r"/private/etc/hosts"

with open(hosts_path, "a") as file:
    for i in range(len(blocked_websites)):
        file.write("\n127.0.0.1 " + blocked_websites[i])
