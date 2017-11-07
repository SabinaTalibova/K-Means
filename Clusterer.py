
from ReadData import ReadData #imported our own class for reading data
import random 
import math
import matplotlib.pyplot as plt #for plotting

class Clusterer:
    def __init__(self):
        self.data=ReadData().please_read_data()
        
        self.cluster1=[] #define cluster array so we can cluster elements to them
        self.cluster2=[]
        self.cluster3=[]
        self.centroid1=[] #define centroid array so we can update them
        self.centroid2=[]
        self.centroid3=[]

    def please_first_iter(self): #I wrote first iteration manually(Tried either way, but I failed to do so)
        for i in self.data:

            self.centroid1=self.please_choose_random_centroid()[0] #for only first iteration I want to initialize centroids with random centroids
            self.centroid2=self.please_choose_random_centroid()[1]
            self.centroid3=self.please_choose_random_centroid()[2]

            #below I found distance between each data element and centroid
            dis_1=math.sqrt((i[0]-self.centroid1[0])*(i[0]-self.centroid1[0])+(i[1]-self.centroid1[1])*(i[1]-self.centroid1[1]))
            dis_2=math.sqrt((i[0]-self.centroid2[0])*(i[0]-self.centroid2[0])+(i[1]-self.centroid2[1])*(i[1]-self.centroid2[1]))
            dis_3=math.sqrt((i[0]-self.centroid3[0])*(i[0]-self.centroid3[0])+(i[1]-self.centroid3[1])*(i[1]-self.centroid3[1]))
            dist=[dis_1,dis_2,dis_3]
            d=sorted(dist)
            min=d[0]
            #I sorted array because I want to find index of minimum element, so I can append to the corresponding cluster
            if dist.index(min)==0:
                self.cluster1.append(i)
            elif dist.index(min)==1:
                self.cluster2.append(i)
            else:
                self.cluster3.append(i)
        

    #this function helps to choose random centroid from dataset itself
    def please_choose_random_centroid(self):
        centroid=random.sample(self.data,3)
        return centroid
    #this function clusters elements(like first iteration, the only difference I use updated centroids not random ones)
    def please_cluster(self):
        
        for i in self.data:
           
            
            dis_1=math.sqrt((i[0]-self.centroid1[0])*(i[0]-self.centroid1[0])+(i[1]-self.centroid1[1])*(i[1]-self.centroid1[1]))
            dis_2=math.sqrt((i[0]-self.centroid2[0])*(i[0]-self.centroid2[0])+(i[1]-self.centroid2[1])*(i[1]-self.centroid2[1]))
            dis_3=math.sqrt((i[0]-self.centroid3[0])*(i[0]-self.centroid3[0])+(i[1]-self.centroid3[1])*(i[1]-self.centroid3[1]))
            dist=[dis_1,dis_2,dis_3]
            d=sorted(dist)
            min=d[0]

            if dist.index(min)==0:
                self.cluster1.append(i)
            elif dist.index(min)==1:
                self.cluster2.append(i)
            else:
                self.cluster3.append(i)
        
    #here I update centroids by finding mean of clusters
    def please_update_centroids(self):
                
        mean1=[sum(clus)/len(clus) for clus in zip(*self.cluster1)]
        mean2=[sum(clus)/len(clus) for clus in zip(*self.cluster2)]
        mean3=[sum(clus)/len(clus) for clus in zip(*self.cluster3)]
        self.centroid1=mean1
        self.centroid2=mean2
        self.centroid3=mean3
        return(mean1,mean2,mean3)
        

    

    
#created object of Clusterer class
ob=Clusterer()
#I first iterate and cluster data
ob.please_first_iter()
counter=0

#I am ashamed to say that I iterate through fixed number(5) of times

while counter<7:
    #3. I empty cluster array
    ob.cluster1=[]
    ob.cluster2=[]
    ob.cluster3=[]
    #1. I cluster elements
    ob.please_cluster()
    #2. then update centroids
    ob.please_update_centroids()
    

    counter+=1

    #for every cluster I find x and y elements 

    x_cl1=[x[0] for x in ob.cluster1]
    y_cl1=[x[1] for x in ob.cluster1]

    x_cl2=[x[0] for x in ob.cluster2]
    y_cl2=[x[1] for x in ob.cluster2]

    x_cl3=[x[0] for x in ob.cluster3]
    y_cl3=[x[1] for x in ob.cluster3]

    #draw each element with specific color
    plt.scatter(x_cl1,y_cl1,c="#2124e1")
    plt.scatter(x_cl2,y_cl2,c="#48bf2d")
    plt.scatter(x_cl3,y_cl3,c="#1c1413")
    #show graph
    plt.show()

    #I draw graph inside while because I want it to draw graph for each iteration


print(ob.cluster3)







