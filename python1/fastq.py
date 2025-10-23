#!/usr/bin/env
total_seqid=0
nt_count=0
characters=0
with open("Python_06.fastq","r") as fastq_obj:

   for line in fastq_obj:
        line = line.rstrip()
        characters+=len(line)
        # if tot_line%4 == 1:
        #     nt_count=len(line)
        #     print(f"for {tot_line} is {line}")
        #     tot_line+=1
        #     total_nt=sum(nt_count)
# print(nt_count)
# id_total=(tot_line/4)
# print(tot_line)  
# print(id_total)
# print(total_nt) 


#num_lines=len(line)
print(characters)
   
# A=line.count('A')
#total_A += A
#num_lines=len(line)

