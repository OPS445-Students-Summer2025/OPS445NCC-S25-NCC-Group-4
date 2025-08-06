#!/usr/bin/env python3
# Student ID: jgylagan
# Assignment 2 NCC Group 4
# Logging Function

from datetime import datetime  # for timestamps
import os  # for folder and path handling

def write_log(message):
        # make a timestamp for filename and inside the log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

            # build path to the desktop folder where logs will go
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    log_folder = os.path.join(desktop_path, "Log_History")
            # Log_History folder on user desktop will contain log files

                
    os.makedirs(log_folder, exist_ok=True)  # if folder doesn’t exist, make it


    
    filename = f"log_{timestamp}.txt"   # log file name with timestamp
    log_path = os.path.join(log_folder, filename)

    
    log_entry = f"[{timestamp}] {message}"  # format how the log will look inside the file

        # write the log to the file
    with open(log_path, "w") as f:
        f.write(log_entry + "\n")

    
    print(f"log written to: {log_path}")  # terminal confirmation for user

# if running logging scriptt directly,function declares with sample message
if __name__ == "__main__":
    write_log("Logged Successfully.")