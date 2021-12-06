from collections import Counter
import numpy as np
import itertools
import textwrap




file=open('3_input_fasta_poolprimer.txt', 'r')




def single_repetitions(range_, start_coordinate, string,dict_single_repetitions):
	list_ripetitions=string[start_coordinate:start_coordinate+range_]
	for x in Counter(list_ripetitions).values():
		if x==range_:
			dict_single_repetitions[start_coordinate]='1 BASE x  '+str(range_)+ ' TIMES,  HAVE BEEN COUNTED '


def split_non_consequtive(data):
    data = iter(data)
    val = next(data)
    chunk = []
    try:
        while True:
            chunk.append(val)
            val = next(data)
            if val != chunk[-1] + 1:
                yield chunk
                chunk = []
    except StopIteration:
        if chunk:
            yield chunk


def divide_chunks(l, n): 
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  

def list_positions(x,y,number_repetitions_to_search, list_count):
	lista_repetitions=x[y:y+number_repetitions_to_search*2]

	if len(lista_repetitions)==number_repetitions_to_search*2:
		splitted_text_in_subtext_CTRL_or_TWO=textwrap.wrap(lista_repetitions, int(len(lista_repetitions)/number_repetitions_to_search))
		if number_repetitions_to_search==2:
			if splitted_text_in_subtext_CTRL_or_TWO[0]==splitted_text_in_subtext_CTRL_or_TWO[1] and len(set(splitted_text_in_subtext_CTRL_or_TWO[0]))>1:
				list_count.append(y)
		elif number_repetitions_to_search>2:
			if len(set(splitted_text_in_subtext_CTRL_or_TWO))>1:
				splitted_text_in_subtext_COUNT=textwrap.wrap(lista_repetitions, int(len(lista_repetitions)/2))
				if splitted_text_in_subtext_COUNT[0]==splitted_text_in_subtext_COUNT[1]:
					print(y,splitted_text_in_subtext_COUNT, len(splitted_text_in_subtext_COUNT[0]))
					list_count.append(y)





def repetition_counts(lista_count_repetitions,repetitions_number,output_repetitions):
	#print(lista_count_repetitions)

	if len(lista_count_repetitions)>0:
		for a in split_non_consequtive(lista_count_repetitions):
			
			if len(a) ==1:
				output_repetitions.append(int((0+repetitions_number*2)/repetitions_number))
			else:
				num_start=a[0]
				num_end=a[-1]
				print(num_start,num_end)
				if (num_end % 2) == 0:
					output_repetitions.append(int((num_end-num_start+(repetitions_number*2))/repetitions_number))
				else:
					output_repetitions.append(int(((num_end-num_start+((repetitions_number*2))-1)/repetitions_number)))





for x in file:
	if len(x)==0:
		pass
	else:
	    if 'chr' in x:
	    	print(x.strip())
	    else:
	    	print(x.strip())
	    	dict_single_repetitions={}
	    	lista_2_count_repetitions=[]
	    	lista_3_count_repetitions=[]
	    	lista_4_count_repetitions=[]
	    	lista_5_count_repetitions=[]
	    	lista_6_count_repetitions=[]
	    	lista_7_count_repetitions=[]
	    	lista_8_count_repetitions=[]
	    	lista_9_count_repetitions=[]
	    	lista_10_count_repetitions=[]
	    	
	    	for y in range(len(x)):
	    		
	    		lista_single_repetitions=x[y:y+2]### lista sinle repetition			
	    		for z in Counter(lista_single_repetitions).values():
	    			if z==2:
	    				for rep in range(3,len(x)+1):
	    					single_repetitions(rep,y,x,dict_single_repetitions)
	    		list_positions(x,y, 2,lista_2_count_repetitions)
	    		list_positions(x,y, 3,lista_3_count_repetitions)
	    		list_positions(x,y, 4,lista_4_count_repetitions)
	    		list_positions(x,y, 5,lista_5_count_repetitions)
	    		list_positions(x,y, 6,lista_6_count_repetitions)
	    		list_positions(x,y, 7,lista_7_count_repetitions)
	    		list_positions(x,y, 8,lista_8_count_repetitions)
	    		list_positions(x,y, 9,lista_9_count_repetitions)
	    		list_positions(x,y, 10,lista_10_count_repetitions)
	    	


	    	listexcluded=[]
	    	for a in dict_single_repetitions.items():
	    		for b in dict_single_repetitions.items():
	    			if a[0]-1 ==b[0]:
	    				listexcluded.append(a[0])
	    	for c in listexcluded:
	    		dict_single_repetitions.pop(c)
	    	list_output_singlerepetitions=[]
	    	for a in dict_single_repetitions.values():
	    		list_output_singlerepetitions.append(a)
	    	for a in Counter(sorted(list_output_singlerepetitions)).items():
	    		print(a[0],a[1])




	    	output_2_repetitions=[]
	    	repetition_counts(lista_2_count_repetitions,2,output_2_repetitions)
	    	for a in Counter(output_2_repetitions).items():
	    		print( str(2)+' BASES x',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])

	    	output_3_repetitions=[]
	    	repetition_counts(lista_3_count_repetitions,3,output_3_repetitions)
	    	for a in Counter(output_3_repetitions).items():
	    		print( str(3)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_4_repetitions=[]
	    	repetition_counts(lista_4_count_repetitions,4,output_4_repetitions)
	    	for a in Counter(output_4_repetitions).items():
	    		print( str(4)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_5_repetitions=[]
	    	repetition_counts(lista_5_count_repetitions,5,output_5_repetitions)
	    	for a in Counter(output_5_repetitions).items():
	    		print( str(5)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_6_repetitions=[]
	    	repetition_counts(lista_6_count_repetitions,6,output_6_repetitions)
	    	for a in Counter(output_6_repetitions).items():
	    		print( str(6)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_7_repetitions=[]
	    	repetition_counts(lista_7_count_repetitions,7,output_7_repetitions)
	    	for a in Counter(output_7_repetitions).items():
	    		print( str(7)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_8_repetitions=[]
	    	repetition_counts(lista_8_count_repetitions,8,output_8_repetitions)
	    	for a in Counter(output_8_repetitions).items():
	    		print( str(8)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_9_repetitions=[]
	    	repetition_counts(lista_9_count_repetitions,9,output_9_repetitions)
	    	for a in Counter(output_9_repetitions).items():
	    		print( str(9)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])
	    	output_10_repetitions=[]
	    	repetition_counts(lista_10_count_repetitions,10,output_10_repetitions)
	    	for a in Counter(output_10_repetitions).items():
	    		print( str(10)+' BASES x ',list(a)[0],'TIMES, HAVE BEEN COUNTED ',list(a)[1])	    			
	    	
	    	
	    	

	    	