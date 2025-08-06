import shutil
import os
import tarfile 


def confirm_overwrite(path):
#when a file with the same name is there prompt user to overwrite
    if not os.path.exists(path):
        return True  # No file to overwrite, so no need to ask
    while True:
        response = input("File already exists. Overwrite? [y/n]: ").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


#backup function 
def create_backup(source_path, backup_path):

    #if the path does not exist then give error
    if not os.path.exists(source_path):
        print(f"Source path {source_path} does not exist!")
        return
    
    #if user inputed n into the overwrite prompt cancels backup
    if not confirm_overwrite(backup_path):
        print("Backup cancelled.")
        return
    
    #if user inputs a directory and not a file backups the whole directory
    if os.path.isdir(source_path):
        shutil.copytree(source_path, backup_path)
        print(f"Directory backup created at: {backup_path}")
    #if user inputs a file and not a directory backups the whole directory
    elif os.path.isfile(source_path):
        shutil.copy2(source_path, backup_path)
        print(f"File backup created at: {backup_path}")
    else:
        print(f"Invalid source path: {source_path}")

# Restores files and uncompresses if need be
def restore_backup(backup_path, restore_path):
    #if user inputs a directory and not a file restores the whole directory
    if os.path.isdir(backup_path):
        shutil.copytree(backup_path, restore_path)
        print(f"Directory restored at: {restore_path}")
    
    #if user inputs a file and not a directory restores the whole directory    
    elif os.path.isfile(backup_path):
        shutil.copy2(backup_path, restore_path)
        print(f"File restored at: {restore_path}")
    else:
        print(f"Invalid backup path: {backup_path}")

# Example usage
if __name__ == "__main__":
    while True:
        choice = input("Do you want to (b)ackup or (r)estore? (enter 'b' or 'r'): ").strip().lower()
        if choice == 'b':
            source_path = input("Enter the source file/directory path to back up: ").strip()
            backup_path = input("Enter the backup destination path: ").strip()
            create_backup(source_path, backup_path)
            break
        elif choice == 'r':
            backup_path = input("Enter the backup file/directory path to restore from: ").strip()
            restore_path = input("Enter the restore destination path: ").strip()
            restore_backup(backup_path, restore_path)
            break
        else:
            print("Invalid input. Please enter 'b' for backup or 'r' for restore.")
