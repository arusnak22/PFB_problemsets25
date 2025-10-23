#!usr/bin/env python3
import re 
import pprint
codons={}
with open ("python_08.fasta","r") as codon_obj:
    for line in codon_obj:
        line=line.rstrip()
        if line.startswith('>'):
            id=re.search(r"[>](\S+)",line)
            gene_name=id.group(1)
            codons[gene_name]=[]
        else:
            codons[gene_name]+=re.findall(r"(.{1,3})",line)
    for gene_name in codons:
        seq = codons[gene_name]
        seq1=seq[0:6]
        codons[gene_name]=seq1
        
    for id,seq in codons.items():
        combined=''.join(seq)
        reverse=combined[::-1]
        lower_case=reverse.replace('A','t').replace('T','a').replace('G','c').replace('C','g') 
        compliment=lower_case.upper()
        final=re.findall(r"(.{1,3})",compliment)  
        codons[id]=final
        
    pprint.pprint(codons)
    
        #pprint.pprint(codons)
