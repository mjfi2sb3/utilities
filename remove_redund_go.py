#!/bin/env python

import sys
import argparse
from collections import defaultdict


thisFile = __file__

def main(argv):
	inputfile = ""
	outputfile = ""
	
	parser = argparse.ArgumentParser(description="This script will consolidate a two col tabular file where the first column contains gene ids and second column contains annotated GO terms.")
	parser.add_argument('-i', '--input', action='store', required=True, help='input file')
	#parser.add_argument('-o', '--output', action='store', required=True, help='output file')

	args = parser.parse_args()

	#in= open()
	#if args.input == args.output:
		#sys.exit("Input and output files must be different")
	
	fIn = open(args.input,"r")
	
	goDict = defaultdict(list)
	for line in fIn:
		line = line.strip('\n') # remove \n at the end
		cols= [] # decalre list to hold the two columns
		cols = line.split('\t')
		cols2 = [] # declare second list to store GO terms in second column
		cols2 = cols[1].split("|") # split go terms by column
		#goDict[cols[0]].extend(cols2)
		goDict[cols[0]] = list(set(cols2 + goDict[cols[0]]))
		#print cols[0]," >>>>> ",goDict[cols[0]]
		#print "######################"
	fIn.close()
	
	for key, value in goDict.iteritems():
		#print key," >>> ", value
		print key,"\t"+";".join(value)


if __name__ == "__main__":
	main(sys.argv[1:])