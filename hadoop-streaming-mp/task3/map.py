#!/usr/bin/env python
import sys
import string
import csv

csv_reader= csv.reader(sys.stdin, delimiter=',')
for cells in csv_reader:
    s=cells[2]
    due=cells[12]
    
    print ('%s\t%s' % (s,due))