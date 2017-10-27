import tkinter
import numpy

def found(mo,no,ra):
	f1=open("movie.txt",'w')
	for i in range(0,len(mo)):
		f1.write(mo[i]+","+str(no[i])+","+str(ra[i])+"\n")
	f1.close()

def nofo(mo,no,ra):
	f1=open("movie.txt",'a')
	x=len(mo)-1
	f1.write(mo[x]+","+str(no[x])+","+str(ra[x])+"\n")
	f1.close()

def mains(m,r):
	f=open("movie.txt",'r')
	l2=tkinter.Label(top,text="You might like :",bg='Green')
	ind=0
	fd=0
	ct=0
	mo=list()
	no=list()
	ra=list()
	det=list()
	#m=input("Enter movie name : ")
	det.append(m)
	#r=float(input("Enter the rating : "))
	for x in f.readlines():
		l=x.split(',')
		mo.append(l[0])
		no.append(int(l[1]))
		ra.append(float(l[2]))
		if l[0].lower()==m.lower():
			fd=1
			ind=ct
		ct+=1
	if fd==1:
		no[ind]+=1
		det.append(no[ind])
		ra[ind]=(((ra[ind]*no[ind])+r)/(no[ind]+1))
		det.append(ra[ind])
		found(mo,no,ra)
		
	else:
		mo.append(m)
		no.append(1)
		det.append(1)
		ra.append(r)
		det.append(r)
		ind=len(mo)-1
		nofo(mo,no,ra)

	ex=ind
	ind=0
	medpoor=2
	medavg=5
	medgood=7
	medexcel=9
	cat=list()
	poor=list()
	aveg=list()
	good=list()
	excel=list()
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
	if det in poor:
		np=list()
		for x in poor:
			np.append(((((no[ex]-x[1])**2)+((ra[ex]-x[2])**2)**0.5)))	
		mov1=1000
		mov2=1000
		mov3=1000
		mov4=1000
		mov5=1000
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
	"""s=int(input("Press 0 to stop or 1 to continue! "))
	if s==0:
		cont=False"""
	f.close()


top=tkinter.Tk()

m="World"
r=-1.0

from tkinter import messagebox

top.geometry("1000x800")
top.title('Movie reviews')

def prins(c):
	global m
	m=c.widget.get()

def prins2(a):
	global r
	r=float(a.widget.get())
	if r<0 or r>10:
		er=tkinter.messagebox.showinfo('Error!','Enter a valid rating')

def hell():
	global m,r
	m=c.get()
	r=float(c2.get())
	if(m=='World'):
		er=tkinter.messagebox.showinfo('Error!','Enter a valid movie')
	elif r<0 and r>10:
		er=tkinter.messagebox.showinfo('Error!','Enter a valid rating')
	else:
		mains(m,r)
			
l1=tkinter.Label(top,text="Enter movie :")
l1.pack(side='left')
l1.place(x=0,y=0)

c=tkinter.Entry(top,bg="Green")
c.pack(side='right')
c.place(x=150,y=0)
c.bind("<Return>",prins)

l2=tkinter.Label(top,text="Enter rating : ")
l2.pack(side='left')
l2.place(x=0,y=20)

c2=tkinter.Entry(top,bg='Blue',fg='White')
c2.bind("<Return>",prins2)
c2.pack(side='right')
c2.place(x=150,y=20)

b=tkinter.Button(top,text='Enter',command=hell)
b.pack()
b.place(x=50,y=60)

top.mainloop()
