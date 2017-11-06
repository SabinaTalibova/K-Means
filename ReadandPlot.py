import matplotlib.pyplot as plt
import random 
import numpy as np
import math 

#assign array which will store data.
data=[]

#read file 
file=open('C:/Users/Sabina/Desktop/K-Means/data_for_exercise4.txt','r')
#file consists of n lines and each line there is two values(see .txt document)
#we need go through file. We do it for loop
#loop will iterate through each "line"(we defined it ourselves) in for loop
#I want  to store data as tuples in "data" array

for line in file:

	l=line.split() #I split line by space. L will be tuple(containing vlues of each line)


	loc=(float(l[0].replace(',','.')),float(l[1].replace(',','.'))) #So this is tuple
	data.append(loc)# append tuple to array



#print(data)#print data
#now I want to plot graph of this data

#draw dataset
x_val_data=[x[0] for x in data]
y_val_data=[x[1] for x in data]

#plt.scatter(x_val_data,y_val_data)

#initialize random centroids and draw them with different color on the same graph
#if I call plt.show() two times, i will get two diferent graph for each scatter
#one show will result all data in one graph
centroids=random.sample(data,3)
x_val_c=[x[0] for x in centroids]
y_val_c=[x[1] for x in centroids]








cent1=[]
tempcent=[]
cent2=[]
cent3=[]
c1=centroids[0]
c2=centroids[1]
c3=centroids[2]
m1=0
m2=0
m3=0




while sorted(tempcent)==sorted(cent1)
    for i in data:
        d1=math.sqrt(((i[0]-c1[0])*(i[0]-c1[0])+(i[1]-c1[1])*(i[1]-c1[1])))
        d2=math.sqrt(((i[0]-c2[0])*(i[0]-c2[0])+(i[1]-c2[1])*(i[1]-c2[1])))
        d3=math.sqrt(((i[0]-c3[0])*(i[0]-c3[0])+(i[1]-c3[1])*(i[1]-c3[1])))
    #print(i)
        if d1<d2 and d1<d3:
            cent1.append(i)
            tempcent.append(i)
        elif d2<d1 and d2<d3:
            cent2.append(i)
        else:
            cent3.append(i)


    m1=[sum(v)/len(v) for v in zip(*cent1)]
    m2=[sum(v)/len(v)  for v in zip(*cent2)]
    m3=[sum(v)/len(v) for v in zip(*cent3)]


    c1=m1
    c2=m2
    c3=m3





    x_new=[x[0] for x in cent1]

    y_new=[x[1] for x in cent1]
    x_new1=[x[0] for x in cent2]
    y_new1=[x[1] for x in cent2]
    x_new2=[x[0] for x in cent3]
    y_new2=[x[1] for x in cent3]

    plt.scatter(x_val_c,y_val_c,c="#c31907")

    plt.scatter(x_new,y_new,c="#2124e1")
    plt.scatter(x_new1,y_new1,c="#48bf2d")
    plt.scatter(x_new2,y_new2,c="#1c1413")


    plt.show()


