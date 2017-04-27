#!/usr/bin/env python
import sys
import csv   
    
current_key = None


for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    value=float(value)
    if current_key==None:
        current_key=key
        due_list=[]
        due_list.append(value)
    elif current_key==key:
        due_list.append(value)
    else:
        total=sum(due_list)
        average=total/len(due_list)
        # print('%s\t%s,%s' % (current_key,round(total,2),round(average,2)))
        print('%s\t%.2f, %.2f' % (current_key,round(total,2),round(average,2)))
        current_key=key
        due_list=[]
        due_list.append(value)

total=sum(due_list)
average=total/len(due_list)
print('%s\t%.2f, %.2f' % (current_key,round(total,2),round(average,2)))       
