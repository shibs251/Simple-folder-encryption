
#The purpose of this script is too encrpt the contents of any folder the script is run in 
import os
from cryptography.fernet import Fernet
#find the files
files = []
#loop through the folder and add all files to a list
for file in os.listdir():
	#don't include these three files
	if file =="folderLock.py" or file == "thekey.key" or file == "unlock.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

#generate a key
key = Fernet.generate_key()

#create a file wit hte key as its content
with open("thekey.key", "wb") as thekey:
	thekey.write(key)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
#don't forget to change the default  password in the unlock script

