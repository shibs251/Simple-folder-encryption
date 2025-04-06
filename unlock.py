
#The purpose of this script is too decrypt the contents of the folder folderLock was run in 
import os
from cryptography.fernet import Fernet
#find the files
files = []
#loop through the folder and add all files to a list
for file in os.listdir():
	#don't include these three files
	if file == "folderLock.py" or file == "thekey.key" or file == "unlock.py":
		continue
	if os.path.isfile(file):
		files.append(file)


with open("thekey.key", "rb") as key:
	secretkey = key.read()
#reset default password
password = "password1234"

whatsPassword = input("Whats the password bitch?\n")

#decrypt everything
if whatsPassword == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
#wrong password
else:
	print("Fuck off")
