import subprocess
import time
import os

print("""Enter all blocked sites inside "blocked_sites.txt" file.
Follow the format of "www.website.domain" (i.e. www.youtube.com).
~
~
~
""")

timer = input("Please enter time in minutes: ")

with open("timer.txt", "w") as file:
    file.write(timer)

print("\n\nThese websites will be blocked: ")

with open("blocked_sites.txt", "r") as file:
    for line in file:
        print(line, end="")

print("\n~\n~\n~")
print("This program will close in 5 seconds, please run 'blocker.exe' as ADMINISTRATOR to block the websites.")

time.sleep(5)
