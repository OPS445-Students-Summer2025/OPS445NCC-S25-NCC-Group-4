import shutil
import os
import tarfile 
from logtool import write_log

def confirm_overwrite(path):
#when a file with the same name is there prompt user to overwrite
    if not os.path.exists(path):
        return True  # No file to overwrite, so no need to ask
    while True:
        prompt = input("File already exists. Overwrite? [y/n]: ").strip().lower()
        if prompt == 'y':
            return True
        elif prompt == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")



#backup function 
def create_backup(source_path, backup_path):

    #if the path does not exist then give error
    if not os.path.exists(source_path):
        print(f"Source path {source_path} does not exist!")
        return
    
    #asks user if they want make their backup a tar file
    while True:
        choice = input("Back up normally or compress as tar.gz? (enter 'normal' or 'tar'): ").strip().lower()
        if choice in ('normal', 'tar'):
            break
        print("Invalid input. Please enter 'normal' or 'tar'.")
    
    if choice == 'tar':

        

        # if the file is not tar file make it a tar file
        if not backup_path.endswith('.tar.gz'):
            backup_path += '.tar.gz'
        if not confirm_overwrite(backup_path):
            print("Backup cancelled.")
            return
        
        try:
            #writes into the file name and adds a tar extension
            with tarfile.open(backup_path, "w:gz") as tar:
                base_name = os.path.basename(source_path.rstrip(os.sep))
                tar.add(source_path, arcname=base_name)
            print(f"Compressed backup created at: {backup_path}")
            write_log("backup", backup_path, "Backup completed successfully.") 
            
        except FileNotFoundError:
                    print(f"Failed to tar archive file")

    
    #if user inputed n into the overwrite prompt cancels backup
    
   
    else:
        if not confirm_overwrite(backup_path):
            print("Backup cancelled.")


      
            
        #if user inputs a directory backups the whole directory
        if os.path.isdir(source_path):
            shutil.copytree(source_path, backup_path)
            print(f"Directory backup created at: {backup_path}")
            write_log("backup", backup_path, "Backup completed successfully.") 
            
         
         #if user inputs a file backups the whole directory
        elif os.path.isfile(source_path):
            shutil.copy2(source_path, backup_path)
            print(f"File backup created at: {backup_path}")
            write_log("backup", backup_path, "Backup completed successfully.") 
            
            
        else:
            print(f"Invalid source path: {source_path}")

# Restores files and uncompresses if need be
def restore_backup(backup_path, restore_path):
    # Check if backup_path is a tar.gz archive
    if os.path.isfile(backup_path) and backup_path.endswith(('.tar.gz', '.tgz')):
        try:
            with tarfile.open(backup_path, "r:gz") as tar:
                tar.extractall(path=restore_path)
            print(f"Tar archive extracted to: {restore_path}")
            write_log("restore", restore_path, "Restore completed successfully.")
            return
        except FileNotFoundError:
                    print(f"Failed to extract tar file")
                    return

    if os.path.isdir(backup_path):
        shutil.copytree(backup_path, restore_path)
        print(f"Directory restored at: {restore_path}")
        write_log("restore", restore_path, "Restore completed successfully.")
    
    #if user inputs a file restores the whole directory    
    elif os.path.isfile(backup_path):
        shutil.copy2(backup_path, restore_path)
        print(f"File restored at: {restore_path}")
        write_log("restore", restore_path, "Restore completed successfully.")
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
