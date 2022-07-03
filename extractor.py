#extracts multiple zips to a destination
from zipfile  import ZipFile
from tkinter import filedialog

#asks for what zip files need to be extracted
zipped_files = filedialog.askopenfilenames(title='Which Files to Unzip', filetypes=[('Zipped Folders', ".zip")])

#asks where to extract files to
target_directory = filedialog.askdirectory(title='Unzip Destination')

#extracts each zip to target
for file in zipped_files:
    ZipFile(file).extractall(target_directory)