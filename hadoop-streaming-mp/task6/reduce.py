#!/usr/bin/python
import sys
import heapq

whole_dict={}
current_key=None


for line in sys.stdin:
	key,value=line.split('\t',1)
	if current_key==None:
		current_key=key
		whole_dict[current_key]=1
	elif current_key==key:
		whole_dict[current_key]+=1
	else:
		whole_dict[key]=1
		current_key=key
	#if key not in whole_dict.keys():
	
	#else:
		#whole_dict[key]+=1

klist=heapq.nlargest(20,whole_dict,key=whole_dict.__getitem__)

for key in klist:
	print('%s\t%d' % (key,whole_dict[key]))

#tuple_list=[(x,y) for x,y in whole_dict.items()]

#tuple_list=sorted(tuple_list,key=lambda tup:tup[1],reverse=True)

#for i in range(20):
	#print('%s\t%s' % (tuple_list[i][0],tuple_list[i][1]))
	