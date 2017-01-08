import os
import json
import shutil

data = {}
with open("Data Collection/old_courses.json") as datafile :
	data = json.load(datafile)

# if(data.has_key("AML100")==1):
# 	print data["AML100"] , data["MAL250"] 





baaproot = "/home/aman/Desktop/PaperDownloader/QuestionPapers"
for file in sorted(os.listdir(baaproot)):
	root  =  baaproot + "/" + file
	for file in sorted(os.listdir(root)):
		if(data.has_key(file)==1):
			oldpath = root + "/" + file
			newpath = root + "/"  + data[file]
			print oldpath, newpath
			shutil.move(oldpath,newpath) 
		