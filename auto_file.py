import os
import shutil

path = input("Enter the path of directory: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    
    if extension in ['mkv', 'mp4']:
        if os.path.exists(path+"/videos"):
            shutil.move(path + "/" + file, path + "/videos/" + file)
        else:
            os.makedirs(path + "/videos") 
            shutil.move(path + "/" + file, path + "/videos/" + file)
    if extension in ['jpg','jpeg','png', 'gif','svg']:
        if os.path.exists(path+"/images"):
            shutil.move(path + "/" + file, path + "/images/" + file)
        else:
            os.makedirs(path + "/images")
            shutil.move(path + "/" + file, path + "/images/" + file)
    else:
        if os.path.exists(path+"/"+extension):
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
        else:
            os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
