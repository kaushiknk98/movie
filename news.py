import csv
import random
f=open('movie.txt','w')
fp=open("mov.csv",'r')
l=list()
ch=0
for x in fp.readlines():
	if ch!=0:
		l=x.split(',')
		f.write((l[1])+',')
		f.write(str(random.randint(1,1000))+',')
		f.write(str(random.uniform(1,10))+'\n')
	else:
		ch=1
f.close()
fp.close()