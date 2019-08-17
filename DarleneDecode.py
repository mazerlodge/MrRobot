#!/usr/local/opt/python/bin/python3.7

# Version: 20170707-1815

# Opens data file and outputs first two letters of every sixth word.

import sys
from ArgTools import ArgParser

# Hard coded constants
DATA_FILE__MAC = "./darlene_code.txt"
DATA_FILE__WIN = ".\\darlene_code.txt"

# Setup variables
osType = "NOT_SET"
dataPath = "NOT_SET"
bDataFileSet = False
wordIndex = -1
charCount = -1
skipChar = "!"

def showUsage():
    print("Usage: python DarleneDecode.py [-os {mac | win} | -file datafile.txt] "
			+ "-wordindex n -charcount c [-skipchar g]\n"
    		+ "\t -os {mac | win} - Operating system selection (used to set dictionary path).\n"
    		+ "\t -file filename.txt - (optional) data file to process.\n"
    		+ "\t -wordindex n - process every n words (e.g. n=5, process every fifth word).\n"    		
			+ "\t -charcount c - retrieve c chars from each word processed.\n"
			+ "\t -skipchar g - (optional) if a target word starts with g, skip that letter when processing.\n")
    exit()

def parseArgs():
	# Parse the arguments looking for required parameters.
	# Return false if any tests fail.
	
	global osType, dataPath, bDataFileSet, wordIndex, charCount, skipChar
	
	subtestResults = []
	rval = True
	
	# Instantiate the ArgParser
	ap = ArgParser(sys.argv)

	# Check for wordIndex
	rv = False
	if (ap.isInArgs("-wordindex", True)):
		wordIndex = int(ap.getArgValue("-wordindex"))
		rv = True
	subtestResults.append(rv)

	# Check for characterCount
	rv = False
	if (ap.isInArgs("-charcount", True)):
		charCount = int(ap.getArgValue("-charcount"))
		rv = True
	subtestResults.append(rv)

	# Check for data file being specified.
	if (ap.isInArgs("-file", True)):
		dataPath = ap.getArgValue("-file")
		bDataFileSet = True
		rv = True
	subtestResults.append(rv)

	if (not bDataFileSet):
		# if no data file specified, check for OS type
		rv = False
		if (ap.isArgWithValue("-os", "mac") or ap.isArgWithValue("-os", "win")):
			osType = ap.getArgValue("-os")
			rv = True
		subtestResults.append(rv)
	
	# Check for optional skipChar
	if (ap.isInArgs("-skipchar", True)):
		skipChar = ap.getArgValue("-skipchar")

	# Determine if all subtests passed
	for idx in range(len(subtestResults)):
		rval = rval and subtestResults[idx]
			
	return(rval)
	
def getDarleneData():

	global dataPath

	if (not bDataFileSet):
		# set data path based on OS
		if (osType == "mac"):
			dataPath = DATA_FILE__MAC 
		else:
			dataPath = DATA_FILE__WIN

	# Read the data
	file = open(dataPath, "r")
	lines = file.readlines()
	file.close()
	
	return(lines)
	
def doDarleneDecode():

	# Determine if a skip char was specified.
	bSkipEnabled = False
	if (skipChar != "!"):
		bSkipEnabled = True

	# Load the data into a lines string
	lines = getDarleneData()
	words = []

	print (len(lines))

	# split words, handling multi-line input and stripping excess whitespace
	for line in lines:
		if (line[0] != "#"):
			rawWords = line.split(' ')
		
			for aword in rawWords:
				if (len(aword.strip(' \n\r\t')) > 0):
					words.append(aword)
	print(words)
		
	# zero based array, so reduce first wordIndex by 1.
	targetwordindex = wordIndex-1 
	while (targetwordindex < len(words)):
		if (bSkipEnabled and (words[targetwordindex][0] == skipChar)):
			# skip the first char in the word 
			print(words[targetwordindex][1:charCount+1], end="")
		else:
			print(words[targetwordindex][0:charCount], end="")
		targetwordindex += wordIndex
			
	print()

#### EXECUTION Starts Here ####

# Validate startup parameters
if (not parseArgs()):
	showUsage()
	exit()

doDarleneDecode()
