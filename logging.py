#!/usr/bin/env python3
# Student ID: jgylagan
# Assignment 2 NCC Group 4
# Logging Function

from datetime import datetime  # for timestamps

def write_log(message):        # function to write a log entry
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")  # year, month day , hour min format
    filename = f"log_{timestamp}.txt" # save as log_y-d-h-m
    
    log_entry = f"[{timestamp}] {message}"  # log entry for the file output

    # create new log  file in the current directory
    with open(filename, "w") as f:
        f.write(log_entry + "\n")  # \n newline formatting

    print(f"Log written to: {filename}")  # show user where the log went, the same directory as the script


if __name__ == "__main__":
    write_log("Logged successfuly.") # terminal confimation


