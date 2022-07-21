##
## Written by Matthew J. Touma
## 7/21/2022
##
## Make sure you close all programs that are using the files to copy BEFORE running the script.

import pdb
import shutil
from datetime import date
from datetime import datetime
import os
from os.path import exists

## =======================================================
## Functions

# This function copies files and directories (recursively) to
# a specified destination.
#
# Inputs:
#   src: Source directory or file path to backup. For individual files,
#        include the filename itself and the extension.
#   dest_dir: Destination directory to copy files to.
def backup(src, dest_dir):
    try:
        #copy entire folder
        if os.path.isdir(src):
            dest_dir = dest_dir + '\\' + (src.split('\\')[-1])
            shutil.copytree(src, dest_dir)

        #copy single file
        elif os.path.isfile(src):
            dest_dir = dest_dir + '\\' + (src.split('\\')[-1])
            shutil.copy2(src, dest_dir)
       
       
    except FileExistsError:
                print("File already exists, skipping.")

## =======================================================
## CHANGE THESE TO FIT YOUR NEEDS                

# Paths to DIRECTORIES that you wish to backup
# These directories including their entire contents will be copied
src = ['C:\\Users\\xxxx\\yourDir0',\
       'C:\\Users\\xxxx\\yourDir1',\
       'C:\\Users\\xxxx\\yourDir2']

# Paths to INDIVIDUAL FILES that you wish to backup
src_ind = ['C:\\Users\\xxxx\\Documents\\yourFile0.txt',\
           'C:\\Users\\xxxx\\Documents\\yourFile1.txt',\
           'C:\\Users\\xxxx\\Documents\\yourFile2.txt']

# Destination directory
dest = 'C:\\Users\\xxxx\\Documents\\Backups Test'

## =======================================================
## Begin Program

print("Backing up...")

# Get the current date and time
today = date.today()
time = datetime.now()
date_time = today.strftime("%Y_%m_%d") + "_" + time.strftime("%H_%M_%S")                                                     

# Create a new folder in the destination directory with the current date and time
new_dest = dest + '\\' + date_time
os.makedirs(new_dest)

print("Backup location: " + new_dest)

# Copy whole directories
for x in src:
    print("Backing up " + x)
    backup(x, new_dest)

# Copy individual files
for x in src_ind:
    print("Backing up " + x)
    backup(x, new_dest)

print("done!")

## FIFO
# Delete old backups if more than 10 backups have been created
if len(next(os.walk(dest))[1]) > 10:
    print("Deleting old backups...")
    shutil.rmtree(dest + '\\' + next(os.walk(dest))[1][0])
    print("done!")



