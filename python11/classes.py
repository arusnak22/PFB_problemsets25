#!/usr/bin/env python3
class DNAsequence(object):
    sequence = 'ATCGATGACGGTACACA'
    seq_name = 'ACTN1'
    organism = "X.laevis"

    def __init__(self, sequence, seq_name, organism):
        self.sequence = sequence.upper()
        self.seq_name = seq_name
        self.seq_name = organism

    def seq_length(self):
        length=len(self.sequence)
        return length

    def nt_cont(self):
        a_count = print(f"A:{self.sequence.count('A')}")
        t_count = print(f"T:{self.sequence.count('T')}")
        g_count = print(f"G:{self.sequence.count('G')}")
        c_count = print(f"C:{self.sequence.count('C')}")
        return a_count, t_count, g_count, c_count
    
    def gc_cont(self):
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        gc_count = (g_count + c_count)
        return gc_count
    
    def fa_format(self):
        fasta= print(f"{self.seq_name}, \t {self.organism}, \n {self.sequence}")
        return fasta 
        


dna_seq_obj = DNAsequence('ATGCAGATTTAGGACACACACAAATT','ATCN3','X.Laevis')


print(dna_seq_obj.sequence)
print(dna_seq_obj.seq_name)
print(dna_seq_obj.organism)
print(dna_seq_obj.seq_length())
dna_seq_obj.nt_cont()
print(f"GC contenet:{dna_seq_obj.gc_cont()}")
dna_seq_obj.fa_format()
