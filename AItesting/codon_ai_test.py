#!/usr/bin/env python3 
import urllib.request

# Standard genetic code (DNA codons → amino acid)
codon_table = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
    'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
    'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}

def reverse_complement(dna: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    comp_map = str.maketrans('ATCGatcg', 'TAGCtagc')
    return dna.translate(comp_map)[::-1]

def translate_dna_to_aa(dna: str) -> str:
    """Translate a DNA sequence (assumed in‑frame) to amino acids."""
    aa = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) != 3:
            break
        aa.append(codon_table.get(codon.upper(), '?'))
    return ''.join(aa)

def process_fasta_url(url: str):
    with urllib.request.urlopen(url) as resp:
        text = resp.read().decode('utf‑8')
    # Parse FASTA (may assume standard >header lines)
    seq_name = None
    seq = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            # process previous
            if seq_name is not None:
                fullseq = ''.join(seq).upper()
                # first 18 bases => first 6 codons
                first18 = fullseq[:18]
                revcomp18 = reverse_complement(first18)
                aa6 = translate_dna_to_aa(revcomp18)
                print(f"{seq_name} {aa6}")
            # start new record
            seq_name = line[1:].split()[0]
            seq = []
        else:
            seq.append(line)
    # process last record
    if seq_name is not None:
        fullseq = ''.join(seq).upper()
        first18 = fullseq[:18]
        revcomp18 = reverse_complement(first18)
        aa6 = translate_dna_to_aa(revcomp18)
        print(f"{seq_name} {aa6}")

if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/prog4biol/pfb2025/master/files/Python_06.seq.txt"
    process_fasta_url(url)


