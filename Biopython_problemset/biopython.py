#!/usr/bin/env python3 

from Bio import SeqIO
for seq_record in SeqIO.parse("biopython.fa","fasta"):
    ID=seq_record.id
    seq_number=(ID.count)
    Length=0
    Length+=len(seq_record)
    print('num_nt',Length)
print('Total number of nucelotides;',Length)
print('num_seq',len(ID))
avg_len=Length/len(ID)
print('Average sequence length:', avg_len)
#trying to find the total nucleotide length still, was trying to add all of the length og the 
# seq-records togethere but it didn't work


    
