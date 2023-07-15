import os
import shutil

source_directory =os.getcwd()
move_to_dir = "D:\Python Programs\task 2"

for file_name in os.listdir(source_directory):
    extensions = os.path.splitext(file_name)
    extensions= extensions.split(".")[1]
    
    move_to =os.path.join(move_to_dir, extensions)
    os.mkdir(move_to, exist_ok= True)

    source_directory=os.path.join(source_directory, file_name)
    move_to = os.path.join(move_to,file_name)
    shutil.move(source_directory,move_to_dir)
