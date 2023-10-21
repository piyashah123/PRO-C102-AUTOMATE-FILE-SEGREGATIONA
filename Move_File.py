import os
import shutil
from_dir = "C:/Users/ADMIN/Pictures/Saved Pictures"
to_dir = "D:/Desktop/white jr/projects/102 PROJ/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

from Move_File in list_of_files:
        name,extension=os.path.splitext(Move_File)
        print(name)
        print(extension)
if extension=="":
    continue
if extension in ['.gif','.png',".jpg"]:
        path1 =from_dir+'/'+ "Move_file"
        path2 =to_dir+'/'+ "Document_files"
        path3 =to_dir+'/'+ "Document_files"+'/'+ "Move_file"
print("path1",path1)
print("path3",path3)

if os.path.exists(path2):
       print("moving" + Document_files + ".....")
       shutil.move(path1,path3)
else:
       os.makedirs(path2)
       print("moving"+ Document_files + "....")
       shutil.move(path1,path3)