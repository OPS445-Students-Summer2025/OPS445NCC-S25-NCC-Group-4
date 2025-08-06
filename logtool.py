#!/usr/bin/env python3
# Student ID: athapa30
# Assignment 2 NCC Group 4
# logtool.py - Logging utility for backup/restore actions

from datetime import datetime
import os

def write_log(operation_type, target_path, message):
    """
    Write a log entry with timestamp, operation type, target path, and message.
    Logs are saved in ~/Desktop/Log_History with a filename including operation type and timestamp.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    log_folder = os.path.join(desktop, "Log_History")
    os.makedirs(log_folder, exist_ok=True)

    filename = f"{operation_type.upper()}_{timestamp}.txt"
    log_path = os.path.join(log_folder, filename)

    log_entry = f"[{timestamp}] [{operation_type}] {target_path}\nMessage: {message}"

    if target_path and os.path.isdir(target_path):
        log_entry += f"\n\nContents of {target_path}:\n"
        for item in os.listdir(target_path):
            full_path = os.path.join(target_path, item)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                log_entry += f"  {item} - {size} bytes\n"
    elif target_path:
        log_entry += f"\n\n[Target folder not found: {target_path}]"

    with open(log_path, "w") as f:
        f.write(log_entry + "\n")

    print(f"log written to: {log_path}")

# For testing logging alone
if __name__ == "__main__":
    write_log("backup", "/home/athapa30/Desktop/testfolder", "Backup test log.")

