import time
import winsound


def write_list_to_file(file_path, content):
    with open(file_path, "w") as file:
        for line in content:
            file.write(line + "")


def read_file_to_list(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    return [line.strip() for line in content]


blocked_path = "blocked_sites"
blocked_websites = read_file_to_list(blocked_path)
hosts_path = r"/private/etc/hosts"

timer_path = "timer"
time_minutes = read_file_to_list(timer_path)

with open(hosts_path, "a") as file:
    for i in range(len(blocked_websites)):
        file.write("\n127.0.0.1 " + blocked_websites[i])

time.sleep(60 * float(time_minutes[0]))

with open(hosts_path, "r") as file:
    hosts_content = file.readlines()

# Remove the blocked websites from the hosts file
hosts_content = [line for line in hosts_content if not any(website in line for website in blocked_websites)]

# Write the updated hosts file
write_list_to_file(hosts_path, hosts_content)
