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

def showUsage():
    print("Usage: python DarleneDecode.py -os {mac | win} \n"
    		+ "\t -os {mac | win} - Operating system selection (used to set dictionary path).\n")
    exit()

def parseArgs():
	# Parse the arguments looking for required parameters.
	# Return false if any tests fail.
	
	global osType
	
	subtestResults = []
	rval = True
	
	# Instantiate the ArgParser
	ap = ArgParser(sys.argv)

	# check the OS type
	rv = False
	if (ap.isArgWithValue("-os", "mac") or ap.isArgWithValue("-os", "win")):
		osType = ap.getArgValue("-os")
		rv = True
	subtestResults.append(rv)
	
	# Determine if all subtests passed
	for idx in range(len(subtestResults)):
		rval = rval and subtestResults[idx]
			
	return(rval)
	
def getDarleneData():

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

	# Load the data into a lines string
	lines = getDarleneData()

	# split words
	for line in lines:
		words = line.split(' ')
		
	targetwordindex = 5 
	while (targetwordindex < len(words)):
		print(words[targetwordindex][0:2], end="")
		targetwordindex += 6
			
	print()

#### EXECUTION Starts Here ####

# Validate startup parameters
if (not parseArgs()):
	showUsage()

doDarleneDecode()
