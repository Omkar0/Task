# Import necessary packages
import sys
import os
import argparse
import shutil
import mysql.connector
    

# Create Folder
def createFolder():
    folderName = input("Enter the folder name: ")
    os.chdir('/home/omkar/Desktop/Task')
    os.mkdir(folderName)


# Create File
def createFile():
    with open('text.txt', 'w') as f:
        wr = input("Enter your first name: ")
        f.write(wr)


# Directories to move file
Current = r'/home/omkar/Desktop/Task/text.txt'
MovingTo = r'/home/omkar/Desktop/folder2/'

# Move File
def moveFile():
    shutil.move(Current, MovingTo)


# MySQL credentials
credential={ 'user':'omkar',

            'password':'omi',

            'database':'Omiee'

          }

# Insert file content to database
def insertIntoDatabase(text):
    cnx = mysql.connector.connect(**credential)
    cursor = cnx.cursor()

    news=text

    query="INSERT INTO leaves (name) VALUES ('"+news+"')"
    cursor.execute(query)

    cnx.commit()
    cursor.close()
    cnx.close()


# Find txt file to add name in database 
def findFile():
    directory='/home/omkar/Desktop/folder2/'

    ls=os.listdir(directory)

    for file in ls:
        if file.endswith(".txt"):
            archive = open(directory+file,'r')
            text=''
            for line in archive:
                text+=line
            insertIntoDatabase(text)
            archive.close()
            print ('Your name is registered in database!!!')


# Full cycle of creating folder, file and move file from current directory to other directory
# & and insert the name value in MySQL database
def Full_process():
    createFolder()
    createFile()
    moveFile()
    findFile()


# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('operation', help="provide operation")
args = parser.parse_args()
# USAGE
# python task1.py createFile
if args.operation == "createFile":
    createFile()
# USAGE
# python task1.py createFolder
elif args.operation == "createFolder":
    createFolder()
# USAGE
# python task1.py moveFile
elif args.operation == "moveFile":
    moveFile()
# USAGE
# python task1.py insertIntoDatabase
elif args.operation == "insertIntoDatabase":
    findFile()
# USAGE
# python task1.py Full
elif args.operation == "Full":
    Full_process()
else:
    pass