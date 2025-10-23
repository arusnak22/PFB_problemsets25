#!/usr/bin/env python3
import re
import pprint
seq_comp={}
with open ("python_08.fasta","r") as py_obj:
    for line in py_obj:
        line = line.rstrip()
        if line.startswith('>'):
            joined=''
            id=re.search(r"[>](\S+)",line)
            gene_name=id.group(1)
        else:
            joined+=line
            a_count=joined.count('A') 
            t_count=joined.count('T')
            g_count=joined.count('G')
            c_count=joined.count('C')
            seq_comp[gene_name]={'A':a_count, 'T':t_count, 'G':g_count,'T':t_count}

pprint.pprint(seq_comp)

