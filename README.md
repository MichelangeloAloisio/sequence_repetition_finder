########################################################################################################################################################################
########################################################################################################################################################################
SEQUENCE REPETITION FINDER_v1 is a python script written in python 3,  useful to define the percentage of repetitions and the GC% in DNA FASTA sequences. 
After the uploading of a fasta sequence (see fasta example in file: sequence.fasta) it reads from file:  
1) coordinate start end of the sequence in order to compute the size;
2) the name of the sequence (in the example is PCR10: >chr1:0-100 PCR10)
3) the sequence.

It analyzes the sequence e counts repetitions from 1 to 10 bases, determining the lenght of repetition and the percentage of repeated element on total of the sequence. 
As example, it finds in sequence AAAATCTCTCAAAA: 4 Adenine repeated 2 time in the sequence and 3 TC repeated 1 time in the sequence.
It computes the percentage of repetions in the sequence, example:14 bases lenght: 8 bases (single bases repeated: 4 (adenine)* 2 times) + 6  ( double bases TC repeated: 2 *3 times);
since the total sequence lenght is 14 bases and the repeated bases in sequence are 14=> 100% of sequence is repeated.
ATTENTION,  the percentage of repetions in the sequence could result >100% and it means the the full sequence is repeated. In the following example, a case of the 
% repetition > 100% is described: - in sequence tccctccc are counted 8 repetitions of 4 bases in tandem (tccc) + 6 repetitions of 3 single bases 2 times (ccc), therefore
on the total lenght of 8 bases: 8 +6 repetions have be counted resulting in 150% of repetitions in sequence.

LAUNCH TOOL: 
1) make a folder containing the fasta file to analyze and sequence_repetition_finder.py file, launch the pipeling inserting the input name in file variable;
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


