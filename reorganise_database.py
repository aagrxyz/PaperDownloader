import os

<<<<<<< HEAD
baaproot = "/home/aman/Desktop/PaperDownloader/QuestionPapers"
for file in sorted(os.listdir(baaproot)):
	root  =  baaproot + "/" + file
	some_var = "aaaaaa"
	# print file
	for file in sorted(os.listdir(root)):
		if file.endswith(".pdf"):
			some_var1 = file[:6].upper()
			# print file
			if some_var == some_var1:
				oldpath = root + "/" + file
				newpath = root + "/" + some_var1 + "/" + file
				os.rename(oldpath,newpath) 
			else:
				os.makedirs(root + "/" + some_var1)
				oldpath = root + "/" + file
				newpath = root + "/" + some_var1 + "/" + file
				os.rename(oldpath,newpath) 
				some_var = some_var1


