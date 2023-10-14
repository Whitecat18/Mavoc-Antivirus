import os
import shutil
import getpass 

def del_temp_files_cli():

    print("Cleaning Temp Files . Please wait !!")

    cur_user = getpass.getuser()

    temp_dir = os.path.join('C:\\Users', cur_user, 'AppData', 'Local', 'Temp')
    temp_dir1 = 'C:\\Windows\\prefetch'
    temp_dir2 = 'C:\\Windows\\Temp'

    temp_paths = [temp_dir , temp_dir1 , temp_dir2]


    for path in temp_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print("File Deleted Successfully")
                except Exception as e:
                    print("Error Deleting the Files")

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted folder: {dir_path}\n")
                except Exception as e:
                    print(f"Error deleting folder: {dir_path}, Error: {e}\n")
    
    print("completed Cleaning System files.\n")

