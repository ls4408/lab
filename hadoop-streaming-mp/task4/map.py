#!/usr/bin/python
import sys
import csv

csv_reader= csv.reader(sys.stdin)
for s in csv_reader:
    if s[16]=='NY':
        print ('%s\t%s' % ('NY',1))
    else:
        print ('%s\t%s' % ('Other',1))
               
    
