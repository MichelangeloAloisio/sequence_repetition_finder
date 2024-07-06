################################################################################################################################################################################
########################################################          2)string_complexity_computing_v1                     #########################################################
####CONTACT michelangelo.aloisio@irccsdebellis.it

import re
from collections import Counter
import numpy as np
import itertools
import textwrap
import pandas as pd

def save_all_elements(search_list):
    lista=[]
    for s in search_list:
        for el in range(s[0],s[1]):
            lista.append(el)
    return lista

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

FILE='sequence.fasta'

file=open(FILE, 'r')

min_repetition=3
lista_index=[]
list_df=[]
size_PCR=[]
gcperc=[]
rep_percentage=[]



for x in file:
    if len(x)<=1:
        pass
    else:
        if '>' in x:
            #lista_index.append('PCR'+x.strip().split('PCR')[1].split('0')[0])
            lista_index.append(x.strip())
            print('READING SEQUENCE: ' +x.strip())
            
        else:
            #print(x.strip(), len(x.strip()))
            formatted_x=x.strip().lower()
            count=0
            for j in formatted_x:               
                if j=='a' or j=='t' or j=='c' or j=='g':
                    count=count+1
            gcperc.append(round((formatted_x.count('c')+formatted_x.count('g'))*100/count,2))
            size_PCR.append(count)
            lista_count_repetitions=[]
            text=list(formatted_x)
            dataframe_STRING={}
            range_interval=range(1,10)#(int(len(formatted_x)/2+1)))#define range interval dividing the String on half of lenght
            for windows_lenght in reversed(range_interval):
                for y in range(len(formatted_x)):
                    lista_repetitions=''.join(text)[y:y+windows_lenght]
                    if len(lista_repetitions)==windows_lenght:
                        if windows_lenght>=1:
                            group=[]
                            search=[m.span() for m in re.finditer(lista_repetitions.lower(),''.join(text))]
                            if len(search)>=min_repetition:#set minimum 2 repetitions contigous and non contigous
                                search_open=save_all_elements(search) ###full list from start-end
                                for gen in split_non_consequtive(search_open):
                                    ctrl_repetitions=int(len(gen)/len(lista_repetitions))
                                    if ctrl_repetitions>=min_repetition:
                                        for change in range(gen[0],gen[-1]+1):
                                                text[change]=text[change].upper()
                                        if len(set(formatted_x[gen[0]:gen[-1]+1]))==1:
                                            lista_count_repetitions.append('1 bp x'+ str(len(gen)))
                                        else:
                                            if (len(formatted_x[gen[0]:gen[-1]+1]) % 2) == 0:
                                                if len(textwrap.wrap(formatted_x[gen[0]:gen[-1]+1], 2))==1:
                                                    lista_count_repetitions.append('2 bp x'+ str(len(textwrap.wrap(formatted_x[gen[0]:gen[-1]+1], 2))))
                                                else:
                                                    lista_count_repetitions.append(str(windows_lenght)+' bp x'+str(len(textwrap.wrap(formatted_x[gen[0]:gen[-1]+1], windows_lenght))))
                                            else:
                                                if len(textwrap.wrap(formatted_x[gen[0]:gen[-1]], 2))==1:
                                                    lista_count_repetitions.append('2 bp x'+ str(len(textwrap.wrap(formatted_x[gen[0]:gen[-1]], 2))))
                                                else:
                                                    lista_count_repetitions.append(str(windows_lenght)+' bp x'+ str(len(textwrap.wrap(formatted_x[gen[0]:gen[-1]], windows_lenght))))
            N_Upper_case=len(re.findall(r'[A-Z]',''.join(text)))
            N_lenght_string=len(''.join(text))
            percentage_upper_case_in_STR=round(N_Upper_case*100/N_lenght_string,1)
            rep_percentage.append(percentage_upper_case_in_STR)

            print(''.join(text))
            for a in Counter(sorted(lista_count_repetitions)).items():
                dataframe_STRING[a[0]]=[a[1]]
            df=pd.DataFrame.from_dict(dataframe_STRING, orient='columns')#columns=None)
            if len(df)==0:
                empty_df={'no_duplicates': [0]}
                df=pd.DataFrame.from_dict(empty_df, orient='columns')
            list_df.append(df)


set_=set()

for x in list_df:
    for y in x.columns:
        set_.add(y)

result = pd.concat(list_df, axis=0,keys=lista_index)


result['amplicon_size']=size_PCR
result['% duplicate sequence']=rep_percentage

result['%GC']=gcperc
result=result.fillna(0)
result.to_excel('output.'+FILE+'.xls')
print(result)






print('OUTPUT FILE IS SAVED IN THE CURRENT FOLDER!!!')
print('THANKS ')
