#!/usr/bin/env python3
import re 
with open ("Python07.fasta","r") as fasta_obj:
    for line in fasta_obj:
        line = line.rstrip()
        #id=re.search(r"^>\S+",line)
        #print(id)
        #print(line)
        seq= re.search(r"\n\w+",line)
        if seq:
            print(seq)
        seq_id =re.search(r"^>(\w+)",line) 
        if seq_id:
            seqName=(seq_id.group(1))
            print(f"id:{seqName}")
        seqdef =re.search(r"\s[WH](.?.+)",line)
        if seqdef:
            desc = (seqdef.group(1))
            print(f"desc:{desc}")