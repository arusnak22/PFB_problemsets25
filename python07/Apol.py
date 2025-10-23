#!/usr/bin/env python3
import re 
snip_count={}
seq=""
with open ("Python_07_Apol.fasta","r") as fasta_obj:
    for line in fasta_obj:
        line=line.rstrip()
        replace=re.sub(r'([AG])(AATT[CT])',r'\1^\2',line)
    # for found in re.finditer(r"[AG]AATT[CT]",contents):
    #     whole = found.group(0)
    #     cut_start = found.start(0)+1
        #print(f"{whole}:{cut_start}")
        if replace.startswith('>'):
            continue
        else:
            seq+=replace
    split=seq.split('^')
    split.sort(key=len)
    print(split)
    
        #new_replace=replace.rstrip()
        #print(new_replace)
        #snips=new_replace.split('^')
        #snip_count['snip1']=(snips[1])

#print(snip_count)
#print(len(snip_count['snip1']))
 
        