#!/usr/bin/env
with open("Python_06.seq.txt","r") as seq_file_obj:
	seq_list=[]
	for line in seq_file_obj:
	 line = line.rstrip()
	 split=line.split()
	 seq_only=split[1]
	 gene=split[0]
	 rev_seq=seq_only[::-1]
	 A_to_t=seq_only.replace('A','t')
	 T_to_a=A_to_t.replace('T','a')
	 G_to_c=T_to_a.replace('G','c')
	 C_to_g=G_to_c.replace('C','g')
	 upper_seq=C_to_g.upper()
	 print(f">{gene}:{upper_seq}")	
# seq_list.append(rev_seq)
	

	 
