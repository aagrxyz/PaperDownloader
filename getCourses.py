import os
import json
import shutil
entry ='2013cs10224'
baaproot = "/home/aman/Desktop/PaperDownloader/QuestionPapers"
output_home_dir = "/home/aman/Desktop/PaperDownloader/output"
output_dir = output_home_dir + "/" + entry.upper()
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
with open("Data Collection/data_base.json") as datafile :
	data = json.load(datafile)

courses  = data[entry.upper()]['courses']
paths =[]
for course in courses:
	dept = course[:3]
	if(dept=='COL'):
		for data_base_cname in sorted(os.listdir(baaproot+"/COL")):
			if (data_base_cname==course):
				shutil.copytree(baaproot+"/COL/" + course, output_dir + "/" + course)

shutil.make_archive(output_home_dir + "/" + entry, 'zip', output_dir)
shutil.rmtree(output_dir)








