#! /usr/bin/env python3

# import modules
import argparse
#import csv
import csv

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via `args` variable

args = parser.parse_args()

# Open the GFF file
with open( args.gff) as fgen:


	# loop over all the lines in the file
	for line in fgen:
		line.rstrip()
		column =line.split('\t')
		type_fea = column[2]
		fea_ini = int(column[3])
		fea_en = int(column[4])
		fea_len	= fea_en - fea_ini + 1
		print(type_fea, fea_len)
	
