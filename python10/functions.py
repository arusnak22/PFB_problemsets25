#!/usr/bin/env python3
import re
dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

seq=dna.replace('\n','')

def dna_seperated(sequence):
    lists = []
    for i in range(0,len(sequence),60):
        lists.append(sequence[i:i+60] +'\n')
        combined_lists= ''.join(lists)       
    return combined_lists

print(f"INPUT:{dna} OUTPUT:{dna_seperated(seq)}")

def max_line_length(sequence,width):
    longest=[]
    for i in range(0,len(sequence),width):
        longest.append(sequence[i:i+width]+'\n')
        combined_longest= ''.join(longest)
    return combined_longest 
        
print(f"INPUT:{seq}, \n width=50,\n OUTPUT:{max_line_length(seq,50)}")   
    
        


def gc_content(sequence):
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    sequence_len = len(sequence)
    gc_content = (c_count + g_count) / sequence_len 
    return gc_content 

print(gc_content(seq))

def reverse(sequence):
    rev_dna=sequence[::-1]
    T_to_a=sequence.replace('T','a')
    A_to_t=T_to_a.replace('A','t')
    G_to_c=A_to_t.replace('G','c')
    C_to_g=G_to_c.replace('C','g')
    compl_dna=C_to_g.upper()
    return compl_dna
print(reverse(seq))
