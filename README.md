########################################################################################################################################################################
########################################################################################################################################################################
SEQUENCE REPETITION FINDER_v1 is a python script written in python 3,  useful to define the percentage of repetitions and the GC% of DNA sequences in FASTA format. 
After the uploading of a fasta sequence (see fasta format example in file: sequence.fasta) it reads from file:  
1) the name of the sequence (in the example is PCR10: >chr1:0-100 PCR10)
2) the sequence string.

As default setting it search, in the upload sequence, 3 or more than 3 repetitions of N-bases (bp). The N-bases windows searched ranging from 1 to 10. For example,
giving as input the string 'aggaaaatctctcggggtata', it search the following number of N-bases:

- N-bases: 10 bp -> none repetions of 10 bp in string; 
- N-bases: 9 bp -> none repetions of 10 bp in string;
- N-bases: 8 bp -> none repetions of 10 bp in string;
- N-bases: 7 bp -> none repetions of 10 bp in string;
- N-bases: 6 bp -> none repetions of 10 bp in string;
- N-bases: 5 bp -> none repetions of 10 bp in string;
- N-bases: 4 bp -> none repetions of 10 bp in string;
- N-bases: 3 bp -> none repetions of 10 bp in string;
- N-bases: 2 bp -> 3  double base repetions 'TC'  counted 1 time in the full string, represented in upper case: aggaaaaTCTCTCggggtata.
- N-bases: 1 bp -> 4 single base repetitions counted 2 times in string the first is 'AAAA' and the second 'GGGG'. The single base repetitions counted  are represented in upper case: aggAAAATCTCTCAAAAtata.  NOTE: the 'gg'  and 'tata' repetitions in string, are not recognized. 


LAUNCH TOOL: 
1) make a folder containing the fasta file to analyze  and sequence_repetition_finder.py file, launch the pipeling inserting the input name in file variable;
2) Check the excel output file in folder.

INPUT FILE: 

1) fasta file: see the example of the sequence.fasta in folder. IMPORTANT: the fasta NAME must be: >chr:START-END sequence_ID. The chr, Start and End are used to compute the
sequence lenght useful to compute the percentage of repetitions.

OUTPUT FILE LEGEND:
1) COLUMN name= type of repetitions ex: 1bp x2= aaa other 3 single nucleotides
	                                     2bp x3= tatata other 2 random bases
	                                     3bp x4= tcctcctcctcc other 3 random not repeated bases
	                                     etcc..
	
'2) COLUMN elements= number of times that the repetition described in the column name,
	                         is occurred in the sequence (identified in ID)
    
'3) COLUMN 'amplicon size'= is the size of amplicon IMPORTANT see formatting of fasta input file, the intestation must to be: >chr1:start-end PCR_ID
    
'4) COLUMN '%duplicate sequence'= percentage of duplicated base in sequence. ATTENTION, if result >100%, could be the following case:
               example - in sequence tccctccc are counted 8+6 repetitions, on 8 bases of the overall sequence: 
                                                              -2x tccc|tccc  (4 different bases)=8 repetitions
                                                              -2x ccc       (3 single bases)=6 repetitions ''')


