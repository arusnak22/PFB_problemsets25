#!/usr/bin/env python3
import re
import pprint
three_rf={}
with open("Python_08.codons-frame-1.nt","r") as codon_obj:
    for key in codon_obj:
       seq=codon_obj[key]
       print(key,seq[0:3])