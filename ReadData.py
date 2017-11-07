class ReadData:
	#this function reads data
	def please_read_data(self):
		data=[] #declare data array
<<<<<<< HEAD
		file=open('C:/Users/Sabina/Desktop/Github/K-Means/data_for_exercise4.txt','r')#open txt file for reading
=======
		file=open('C:/Users/Sabina/Desktop/K-Means/data_for_exercise4.txt','r')#open txt file for reading
>>>>>>> b1d3f2fe9d5e8fee140e1d28acb228361be9aff7
		for line in file:#go through file(line by line)
			tup=line.split() #each line is tuple and seperated by space, so we split it by spcae
			refined_tup=(float(tup[0].replace(',','.')),float(tup[1].replace(',','.'))) #python reads input as string so we need to convert
			#string to float. One more issue floats are given in this format(1,123) however it should be(1.123). So we need to replace , with ,
            
			data.append(refined_tup) #then we append each tiple to our data array
		return data
<<<<<<< HEAD
			
=======
			






	       

>>>>>>> b1d3f2fe9d5e8fee140e1d28acb228361be9aff7
