def parseEntryNo(entryno):
	year = int(entryno[:4])
	dept = entryno[4:7]
	return year, dept

def main():
	entry = raw_input("Enter entry number\n")
	year, dept = parseEntryNo(entry)
	print "Entry Year is", year
	print "Department is", dept

if __name__ == '__main__':
	main()