# movie
#creation of dataset
import csv
import random
f=open('movie.txt','w')
fp=open('mov.csv','r')
#mov.csv is the file that was downloaded from kaggle. It has only the movie names and the cast of the movie so we are using the movie name and assigning the number of viewers and the rating using some random values
l=list()
ch=0
for x in fp.readlines():
	if ch!=0:
		l=x.split(',')
        f.write((l[1])+',')
        #Random integer number betweeen 1-1000 is assigned for the number of users
        f.write(str(random.randint(1,1000))+',')
        #Random number between 1-10 is assigned to each movie
		f.write(str(random.uniform(1,10))+'\n')
	else:
		ch=1
f.close()
fp.close()

#accepting user input and cluster and recommend movies
import tkinter
import numpy

#This function updates the number of users and the average rating in the dataset if the movie entered by the user is already existing in the dataset 
def found(mo,no,ra):
	f1=open("movie.txt",'w')
	for i in range(0,len(mo)):
		f1.write(mo[i]+","+str(no[i])+","+str(ra[i])+"\n")
	f1.close()

#If it is a new movie then it is entered as the last entry in the dataset file 
def nofo(mo,no,ra):
	f1=open("movie.txt",'a')
	x=len(mo)-1
	f1.write(mo[x]+","+str(no[x])+","+str(ra[x])+"\n")
	f1.close()

#m is the movie name entered by the user and r is the rating entered by the user for that movie
def mains(m,r):
	f=open("movie.txt",'r')
	l2=tkinter.Label(top,text="You might like :",bg='Green')
	ind=0
	fd=0
	ct=0
#mo is the list containing all the movie names while the no is the list containing the number of viewers for each of the movies and ra contains the rating for each of the movie     
	mo=list()
	no=list()
	ra=list()
#det list contains the value corresponding to the entry given by the user in the dataset
	det=list()
	det.append(m)
	
	for x in f.readlines():
    #we split the entry in the dataset into a list containing the movie name, number of viewers and rating. Since we get the values as strings we convert the number of viewers into an integer and the rating as the float
        l=x.split(',')
		mo.append(l[0])
		no.append(int(l[1]))
		ra.append(float(l[2]))
    #we use the lower function to ensure that the momvie name is not case sensitive
		if l[0].lower()==m.lower():
			fd=1
#ind is the location of the entry if it already exists in the dataset 
			ind=ct
		ct+=1
	if fd==1:
		no[ind]+=1
		det.append(no[ind])
		ra[ind]=(((ra[ind]*no[ind])+r)/(no[ind]+1))
		det.append(ra[ind])
		found(mo,no,ra)
		
	else:
#adding the entry to the end of the movie,viewers and the rating lists.
		mo.append(m)
		no.append(1)
		det.append(1)
		ra.append(r)
		det.append(r)
		ind=len(mo)-1
		nofo(mo,no,ra)

	ex=ind
	ind=0
#medpoor is the median value for poor cluster
	medpoor=2
#medavg is the median value for average cluster
    medavg=5
#medgood is the median value for good cluster
	medgood=7
#medexcel is the median value for excellent cluster
	medexcel=9
	cat=list()
#poor list contains the movies that come under the poor cluster
	poor=list()
#average list contains the movies that come under the average cluster
	aveg=list()
#good list contains the movies that come under the good cluster
	good=list()
#excel list contains the movies that come under the excellent cluster
    excel=list()
#we calculate the difference beetween the median rating via euclidian distance and the movie is put into the cluster for which the distance calculated is the least and then we re-calculate the median value based on the current content of the cluster i.e. we are including the newly added cluster also in calculating the new median value for the cluster
    for x in ra:
		a=((x-medpoor)**2)**0.5
		b=((x-medavg)**2)**0.5
		c=((x-medgood)**2)**0.5
		d=((x-medexcel)**2)**0.5
		if a<=b and a<=c and a<=d:
			cat.append('poor')
			poor.append([mo[ind],no[ind],ra[ind]])
			tra=list()
			for y in poor:
				tra.append(y[2])
			medpoor=numpy.average(tra)

		elif b<=c and b<=d:
			cat.append('average')
			aveg.append([mo[ind],no[ind],ra[ind]])
			tra=list()
			for y in aveg:
				tra.append(y[2])
			medavg=numpy.average(tra)

		elif c<=d:
			cat.append('good')
			good.append([mo[ind],no[ind],ra[ind]])
			tra=list()
			for y in good:
				tra.append(y[2])
			medgood=numpy.average(tra)

		else:
			cat.append('Excellent')
			excel.append([mo[ind],no[ind],ra[ind]])
			tra=list()
			for y in excel:
				tra.append(y[2])
			medexcel=numpy.average(tra)
		ind+=1
#Now we try to ascertain which cluster actually contains the movie entered by the user	
	if det in poor:
		np=list()
#we find out the difference between the movie entered by the user and the other movies in the list. We calculate the Euclidian distance beetween the number of viewers as well as the rating and the least 4 values are selected accordingly.
		for x in poor:
			np.append(((((no[ex]-x[1])**2)+((ra[ex]-x[2])**2)**0.5)))	
		mov1=1000
		mov2=1000
		mov3=1000
		mov4=1000
		mov5=1000
#the mov list contains the entry numbers that are the closest to the movie entered by the user.
		mov=[0,0,0,0,0]
		i=0
		for x in np:
			if x<=mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=[i]+mov[:4]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=mov1
				mov1=x
			elif x>mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:1]+[i]+mov[1:]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=x
			elif x>mov1 and x>mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:2]+[i]+mov[2:]
				mov5=mov4
				mov4=mov3
				mov3=x
			elif x>mov1 and x>mov2 and x>mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:3]+[i]+mov[3:]
				mov5=mov4
				mov4=x
			elif x>mov1 and x>mov2 and x>mov3 and x>mov4 and x<=mov5:
				mov=mov[:4]
				mov.append(i)
				mov5=x
			i+=1	
		l2.pack()
		l2.place(x=0,y=100)
		j=7
#we refer to the movies in the indexes mentioned by the mov list and we recommend them to the user to watch
		for x in mov:
			if not(poor[x][0]==m):
				lp=tkinter.Label(top,text=poor[x][0])
				lp.pack()
				lp.place(x=5,y=20*j)
				j+=1
	
	elif det in aveg:
		na=list()
		for x in aveg:
			na.append(((((no[ex]-x[1])**2)+((ra[ex]-x[2])**2)**0.5)))	
		mov1=1000
		mov2=1000
		mov3=1000
		mov4=1000
		mov5=1000
	#we refer to the movies in the indexes mentioned by the mov list and we recommend them to the user to watch	
        mov=[0,0,0,0,0]
		i=0
		for x in na:
			if x<=mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=[i]+mov[:4]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=mov1
				mov1=x
			elif x>mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:1]+[i]+mov[1:]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=x
			elif x>mov1 and x>mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:2]+[i]+mov[2:]
				mov5=mov4
				mov4=mov3
				mov3=x
			elif x>mov1 and x>mov2 and x>mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:3]+[i]+mov[3:]
				mov5=mov4
				mov4=x
			elif x>mov1 and x>mov2 and x>mov3 and x>mov4 and x<=mov5:
				mov=mov[:4]
				mov.append(i)
				mov5=x
			i+=1	
		l2.pack()
		l2.place(x=0,y=100)
		j=7
		for x in mov:
			if not(aveg[x][0]==m):
				la=tkinter.Label(top,text=aveg[x][0])
				la.pack()
				la.place(x=5,y=20*j)
				j+=1
	
	elif det in good:
		ng=list()
		for x in good:
			ng.append(((((no[ex]-x[1])**2)+((ra[ex]-x[2])**2)**0.5)))	
		mov1=1000
		mov2=1000
		mov3=1000
		mov4=1000
		mov5=1000
    #we refer to the movies in the indexes mentioned by the mov list and we recommend them to the user to watch
        mov=[0,0,0,0,0]
		i=0
		for x in ng:
			if x<=mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=[i]+mov[:4]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=mov1
				mov1=x
			elif x>mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:1]+[i]+mov[1:]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=x
			elif x>mov1 and x>mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:2]+[i]+mov[2:]
				mov5=mov4
				mov4=mov3
				mov3=x
			elif x>mov1 and x>mov2 and x>mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:3]+[i]+mov[3:]
				mov5=mov4
				mov4=x
			elif x>mov1 and x>mov2 and x>mov3 and x>mov4 and x<=mov5:
				mov=mov[:4]
				mov.append(i)
				mov5=x
			i+=1	
		l2.pack()
		l2.place(x=0,y=100)
		j=7
		for x in mov:
			if not(good[x][0]==m):
				lg=tkinter.Label(top,text=good[x][0])
				lg.pack()
				lg.place(x=5,y=20*j)
				j+=1
	
	elif det in excel:
		ne=list()
		for x in excel:
			ne.append(((((no[ex]-x[1])**2)+((ra[ex]-x[2])**2)**0.5)))		
		mov1=1000
		mov2=1000
		mov3=1000
		mov4=1000
		mov5=1000
    #we refer to the movies in the indexes mentioned by the mov list and we recommend them to the user to watch
		mov=[0,0,0,0,0]
		i=0
		for x in ne:
			if x<=mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=[i]+mov[:4]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=mov1
				mov1=x
			elif x>mov1 and x<=mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:1]+[i]+mov[1:]
				mov5=mov4
				mov4=mov3
				mov3=mov2
				mov2=x
			elif x>mov1 and x>mov2 and x<=mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:2]+[i]+mov[2:]
				mov5=mov4
				mov4=mov3
				mov3=x
			elif x>mov1 and x>mov2 and x>mov3 and x<=mov4 and x<=mov5:
				mov=mov[:4]
				mov=mov[:3]+[i]+mov[3:]
				mov5=mov4
				mov4=x
			elif x>mov1 and x>mov2 and x>mov3 and x>mov4 and x<=mov5:
				mov=mov[:4]
				mov.append(i)
				mov5=x
			i+=1	
		l2.pack()
		l2.place(x=0,y=100)
		j=7
		for x in mov:
			if not(excel[x][0]==m):
				le=tkinter.Label(top,text=excel[x][0])
				le.pack()
				le.place(x=5,y=20*j)
				j+=1
	f.close()

top=tkinter.Tk()

m="World"
r=-1.0

from tkinter import messagebox

top.geometry("1000x800")
top.title('Movie reviews')

#this function is called whenever we press the enter or return key after entering the movie name in the corresponding label
def prins(c):
	global m
	m=c.widget.get()

#this function is called whenever we press the enter or return key after entering the rating in the corresponding label
def prins2(a):
	global r
	r=float(a.widget.get())
	if r<0 or r>10:
		er=tkinter.messagebox.showinfo('Error!','Enter a valid rating')

#this function is called whenever we click on the submit button
def hell():
	global m,r
	m=c.get()
	r=float(c2.get())
#We display an error message if movie name or rating entered by the user is invalid
	if(m=='World'):
		er=tkinter.messagebox.showinfo('Error!','Enter a valid movie')
	elif r<0 and r>10:
		er=tkinter.messagebox.showinfo('Error!','Enter a valid rating')
	else:
		mains(m,r)
			
#label asking the user to enter the movie name 
l1=tkinter.Label(top,text="Enter movie :")
l1.pack(side='left')
l1.place(x=0,y=0)

#Get the movie name 
c=tkinter.Entry(top,bg="Green")
c.pack(side='right')
c.place(x=150,y=0)
c.bind("<Return>",prins)

#label asking the user to enter the rating
l2=tkinter.Label(top,text="Enter rating : ")
l2.pack(side='left')
l2.place(x=0,y=20)

#Get the rating
c2=tkinter.Entry(top,bg='Blue',fg='White')
c2.bind("<Return>",prins2)
c2.pack(side='right')
c2.place(x=150,y=20)

b=tkinter.Button(top,text='Enter',command=hell)
b.pack()
b.place(x=50,y=60)

top.mainloop()
