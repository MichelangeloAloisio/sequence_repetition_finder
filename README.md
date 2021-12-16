########################################################################################################################################################################
########################################################################################################################################################################
SEQUENCE REPETITION FINDER_v1 is a python script useful to define the percentage of repetitions of  DNA sequences in FASTA format. 
After the uploading of a fasta sequence (see fasta format example in the file: sequence.fasta) it reads from file:  
1) the name of the sequence (in the example is PCR10: >chr1:0-100 PCR10)
2) the sequence string.


As a default setting, it searches, for upload sequence, 3 or more repetitions of N-bases (bp). The N-bases windows searched ranging with the default cut-off from 1 to 10. As an example to understand how it works, in the input string 'aggaaaatctctcggggtata', it searches the following number of N-bases:

- N-bases: 10 bp -> none repetitions of 10 bp found; 
- N-bases: 9 bp -> none repetitions of 9 bp found;
- N-bases: 8 bp -> none repetitions of 8 bp found;
- N-bases: 7 bp -> none repetitions of 7 bp found;
- N-bases: 6 bp -> none repetitions of 6 bp found;
- N-bases: 5 bp -> none repetitions of 5 bp found;
- N-bases: 4 bp -> none repetitions of 4 bp found;
- N-bases: 3 bp -> none repetitions of 3 bp found;
- N-bases: 2 bp -> 3  repetitions of 2 bases 'TC'  found 1 time in the full string. They are represented in upper case: aggaaaaTCTCTCggggtata.
- N-bases: 1 bp -> 4 repetitions of 1 bases  counted 2 times in string. The first repetitions is 'AAAA' and the second 'GGGG'. The single base repetitions counted  are represented in upper case: aggAAAATCTCTCAAAAtata.  NOTE: the 'gg'  and 'tata' repetitions in string, are not recognized beacuse are only 2 repetitions (2x 'g' and 2x 'tc'). 


LAUNCH TOOL: 
1) make a new folder containing the fasta input file (sequence.fasta) and sequence_repetition_finder.py, launch the pipeline inserting the custom file, change the input name in file variable (variable FILE, script 2)string_complexity_computing_v1.py;
2) Check the excel output file in the folder.

INPUT FILE: 

1) fasta file: see the example of the sequence.fasta in the folder. 
2) IMPORTANT: it accepts only strings with a,c,g,t characters in lower or upper case.

FILE


OUTPUT FILE LEGEND:
1) COLUMN name= type of repetitions ex: 1bp x2= aaa other 3 single nucleotides
	                                     2bp x3= tatata other 2 random bases
	                                     3bp x4= tcctcctcctcc other 3 random not repeated bases
	                                     etcc..
	
'2) COLUMN elements= number of times that the repetition described in the column name,
	                         is occurred in the sequence (identified in ID)
    
'3) COLUMN 'amplicon size'= is the size of the amplicon.
    
'4) COLUMN '%duplicate sequence'= percentage of the duplicated base in the sequence.
