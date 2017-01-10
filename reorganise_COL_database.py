import os
baaproot = "/home/aman/Desktop/PaperDownloader/QuestionPapers/COL"
for file in sorted(os.listdir(baaproot)):
	root  =  baaproot + "/" + file
	print file
	some_var1 = file[:6].upper()
	oldpath = root
	newpath = baaproot + "/" + some_var1
	os.rename(oldpath,newpath) 
	