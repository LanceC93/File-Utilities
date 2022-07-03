#extracts multiple zips to a destination
import time
from zipfile  import ZipFile
from tkinter import filedialog

#asks for what zip files need to be extracted
print('Select zip files:')
time.sleep(.5)
zipped_files = filedialog.askopenfilenames(title='Which Files to Unzip', filetypes=[('Zipped Folders', ".zip")])

if not zipped_files:
    print("No zip files selected.")
else:
    #asks where to extract files to
    print("Select Destination:")
    time.sleep(.5)
    target_directory = filedialog.askdirectory(title='Unzip Destination')

    if target_directory != "":
        #extracts each zip to target
        for file in zipped_files:
            ZipFile(file).extractall(target_directory)
        print('Extracting Complete')
    else:
        print('No Destination Selected')