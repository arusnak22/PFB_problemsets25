#!/usr/bin/env python3
import pprint
field_names = ('qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits')
def blast_dict(blast):
    with open (blast, 'r') as txt:
        for line in txt: 
            line=line.rstrip()
            if line.startswith('#'):
                continue 
            else:
                this_data=dict(zip(field_names, line.split('\t')))
        return (this_data)
    

dict_200_BL50=blast_dict('ss_rand5-200_v_qfo_BL50.txt')
dict_200_BL62=blast_dict('ss_rand5-200_v_qfo_BL62.txt')
dict_200_VT10=blast_dict('ss_rand5-200_v_qfo_VT10.txt')
dict_200_VT160=blast_dict('ss_rand5-200_v_qfo_VT160.txt')
dict_200_VT20=blast_dict('ss_rand5-200_v_qfo_VT20.txt')
dict_200_VT40=blast_dict('ss_rand5-200_v_qfo_VT40.txt')
dict_200_VT80=blast_dict('ss_rand5-200_v_qfo_VT80.txt')
dict_800_BL50=blast_dict('ss_rand5-800_v_qfo_BL50.txt')
dict_800_BL62=blast_dict('ss_rand5-800_v_qfo_BL62.txt')
dict_800_VT10=blast_dict('ss_rand5-800_v_qfo_VT10.txt')
dict_800_VT160=blast_dict('ss_rand5-800_v_qfo_VT160.txt')
dict_800_VT20=blast_dict('ss_rand5-800_v_qfo_VT20.txt')
dict_800_VT40=blast_dict('ss_rand5-800_v_qfo_VT40.txt')
dict_800_VT80=blast_dict('ss_rand5-800_v_qfo_VT80.txt')


compiled_blast_200={'BL50':dict_200_BL50, 'BL62':dict_200_BL62,'VT10':dict_200_VT10, 'VT160':dict_200_VT160, 'VT20':dict_200_VT20, 'VT80':dict_200_VT80}
#pprint.pprint(compiled_blast_200)


for key in compiled_blast_200:
    pprint.pprint('\t'.join([key[x] for x in ('file','percid','alen','evalue')]))

