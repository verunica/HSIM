#Start of assignment 2


#Link State Routing 

#Vector Distance Routing

#Hot potato Routing
import sys, math, random

def main():
	if (len(sys.argv) < 2):
		raise ValueError('Invalid arguments')

	inputFile = open(sys.argv[1])
	fileArray = []
	for line in inputFile:
		fileArray.append(line.rstrip("\n").split(" "))

# Just doing some testing to see if values are being read in correctly
# Each array position after 0 represents a node
# Position 0 indicates the amount of nodes
# fileArray[i][x] i is node and x are the neighbours

	print(fileArray[1])
	if int(fileArray[1][0]) == 1:
		print("this is correct")
	else:
		print("This method may not work")
	
	
main()
