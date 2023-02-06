import os
import time
import ctypes
import winsound
import subprocess
from ctypes import windll



def block_website(website, minutes):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    blocked_website = "\n127.0.0.1 " + website
    with open(hosts_path, "a") as file:
        file.write(blocked_website)
        print(f"Website blocked successfully for {minutes} minute(s)!")
    print("display turning of")
    time.sleep(3)

    # subprocess.Popen("start /min python your_file_name.py", shell=True)
    # subprocess.call("taskkill /IM main.exe /F", shell=True)
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

    time.sleep(60 * minutes)
    with open(hosts_path, "r") as file:
        lines = file.readlines()
    with open(hosts_path, "w") as file:
        for line in lines:
            if line.strip("\n") != blocked_website.strip("\n"):
                file.write(line)
        print("Website unblocked successfully!")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)



website = input("Enter the website you want to block: ")
minutes = int(input("Enter the number of minutes to block the website: "))
block_website(website, minutes)

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
