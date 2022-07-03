#takes contents of a folder and puts them in the home directory of the folder
from shutil import move
from tkinter import filedialog
import os
import time

#asks for folder to grab contents out of
print('Select Folder:')
time.sleep(.5)
folder = filedialog.askdirectory()

#cuts folder to find directory its in (won't work if in root probably)
index = folder.rfind('/')
destination = folder[0:index]
print(destination)

#moves files
list_files = os.listdir(path=folder)
for file in list_files:
    move(folder+"/"+file,destination)

#cleans up folder at the end
os.rmdir(folder)
print("Finished")