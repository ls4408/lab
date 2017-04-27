#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    cells = line.split(',')
    print ('%s\t%s' % (cells[2],1 ))