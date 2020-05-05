import os

def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"C:\Users\Rahosu\Desktop\Learning Python\Secret Message\MySecretMessage")
	print(file_list)

	#(2) for each file, rename filename

	# Code to show current working directory
	saved_path = os.getcwd()
	print("Current Working Directory is " + saved_path)

	# Change directory
	os.chdir(r"C:\Users\Rahosu\Desktop\Learning Python\Secret Message\MySecretMessage")

	for file_name in file_list:
		os.rename(file_name, file_name.translate(str.maketrans("","","0123456789")))

	# Return directory name
	os.chdir(saved_path)

	print(file_list)

rename_files()
