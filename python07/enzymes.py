#!/usr/bin/env python3
import re
enzymes={}
with open ("enzymes.txt","r") as txt_obj:
    for line in txt_obj:
        line=line.rstrip()
        found=re.search(r"(^.+\s(\(.+\))?)\s+(\S+)",line)
        if found:
            gene=found.group(1)
            enzyme=found.group(3)
            enzymes = {gene:enzyme}
            print(enzymes)
#have to make dictionary with gene as key and enzyme as value  
