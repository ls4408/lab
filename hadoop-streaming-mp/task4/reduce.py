#!/usr/bin/python
import sys

state_dict={'NY':0,'Other':0}
for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t',1)
	state_dict[key]+=1

for state,count in state_dict.items():
	if count!=0:
		print('%s\t%d' %(state,count))





