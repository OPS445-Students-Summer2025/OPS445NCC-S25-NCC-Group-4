import shutil
import os
#the code serves as a proof of concept

#features planned:
#option to zip file with tar
#add user promts such as overwriting promts

# Original backup function 
def create_backup(source_path, backup_path):
    if not os.path.exists(source_path):
        print(f"Source path {source_path} does not exist!")
        return
    
    if os.path.isdir(source_path):
        shutil.copytree(source_path, backup_path)
        print(f"Directory backup created at: {backup_path}")
    elif os.path.isfile(source_path):
        shutil.copy2(source_path, backup_path)
        print(f"File backup created at: {backup_path}")
    else:
        print(f"Invalid source path: {source_path}")

# Simple restore function
def restore_backup(backup_path, restore_path):
    if os.path.isdir(backup_path):
        shutil.copytree(backup_path, restore_path)
        print(f"Directory restored at: {restore_path}")
    elif os.path.isfile(backup_path):
        shutil.copy2(backup_path, restore_path)
        print(f"File restored at: {restore_path}")
    else:
        print(f"Invalid backup path: {backup_path}")

# Example usage
if __name__ == "__main__":
    source_path = "/home/ahassanzadeh-langrud/Desktop/INFO.png"
    backup_path = "/home/ahassanzadeh-langrud/Pictures/INFO_backup.png"
    restore_path = "/home/ahassanzadeh-langrud/Desktop/INFO_restored.png"

    # Create backup
    create_backup(source_path, backup_path)

    # Restore backup
    restore_backup(backup_path, restore_path)
