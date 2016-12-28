import os

baaproot = "C:\Users\SAKET\Desktop\QuestionPapers"
for file in os.listdir(baaproot):
	root  =  baaproot + "\\" + file
	some_var = "aaaaaa"
	for file in os.listdir(root):
		if file.endswith(".pdf"):
			some_var1 = file[:6].upper()
			if some_var == some_var1:
				oldpath = root + "\\" + file
				newpath = root + "\\" + some_var1 + "\\" + file
				os.rename(oldpath,newpath) 
			else:
				os.makedirs(root + "\\" + some_var1)
				oldpath = root + "\\" + file
				newpath = root + "\\" + some_var1 + "\\" + file
				os.rename(oldpath,newpath) 
				some_var = some_var1


