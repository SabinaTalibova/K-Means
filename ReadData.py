#Read Data
#plot data
class ReadData:
	
	def please_read_data(self):
		data=[]
		file=open('C:/Users/Sabina/Desktop/K-Means/data_for_exercise4.txt','r')
		for line in file:
			tup=line.split() #tup-tuple
			refined_tup=(float(tup[0].replace(',','.')),float(tup[1].replace(',','.')))
            
			data.append(refined_tup)
		return data
			

	    
      






	       

