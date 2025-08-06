#!/usr/bin/env python3
# Student ID: jgylagan
# Assignment 2 NCC Group 4
# Logging Function

from datetime import datetime  # timestamps
import os  # folder and path handling
import tarfile  # must read contents of tar.gz tatget

def write_log(operation_type, target_path, message):
     # create a timestamp for naming and logging
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

       # log folder creation on desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    log_folder = os.path.join(desktop_path, "Log_History")
    os.makedirs(log_folder, exist_ok=True)  # make folder if not exist

     # log filename will show the operation type and timestamp
    filename = f"{operation_type.upper()}_{timestamp}.txt"
    log_path = os.path.join(log_folder, filename)
    # logs can be labeled as BACKUP, RESTORE or FAIL

      # set the log entry format
    log_entry = f"[{timestamp}] [{operation_type}] {target_path}\nMessage: {message}"

     # if the path exists, log the file list and sizes
    if target_path and os.path.isdir(target_path):
        log_entry += f"\n\nContents of {target_path}:\n"
        for item in os.listdir(target_path):
            full_path = os.path.join(target_path, item)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                log_entry += f"  {item} - {size} bytes\n"
                
                # to handle targets that are tar.gz
    elif target_path.endswith(".tar.gz") and os.path.isfile(target_path):
        try:
            log_entry += f"\n\nContents of TAR archive {target_path}:\n"
            with tarfile.open(target_path, "r:gz") as tar:
                for member in tar.getmembers():
                    log_entry += f"  {member.name} - {member.size} bytes\n"
        except Exception as e:
            log_entry += f"\n\n[Error reading tar.gz contents: {e}]\n"

    elif target_path:
        log_entry += f"\n\n[Target folder not found: {target_path}]"
        #

    # write log to log_path (on Desktop)
    with open(log_path, "w") as f:
        f.write(log_entry + "\n")

    print(f"log written to: {log_path}")

# main block for testing directly
if __name__ == "__main__":
    write_log("backup", "/home/jgylagan/Desktop/testlogfolder", "Testing - backup/restore complete.")
