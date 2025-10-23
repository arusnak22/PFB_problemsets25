#!usr/bin/env python3
script = {}
with open("python05.fasta","r") as python05_file_obj:
  
    for line in python05_file_obj:	
        line = line.rstrip()
        if line.startswith('>'):
            key=line.lstrip('>')
            script[key] = ""
        else:
            script[key]+=line

print('fastaDict=', script)             
        

