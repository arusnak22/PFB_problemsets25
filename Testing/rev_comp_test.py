#!/usr/bin/env python3 
import pytest
sequence = 'ATGCAGATAGACAGATAGAGAGGAAAAATTTCGCGCGGAATA'
def rev_comp(seq):
    # valid = {'A', 'C', 'G', 'T'}
    # if not set(seq).issubset(valid):
    #      raise ValueError("Invalid characters in sequence")
    # if len(seq) == 0:
    #     return 0
    dna=seq.upper()
    reverse = dna[::-1]
    trans = reverse.replace('A', 't').replace('T','a').replace('G','c').replace('C','g')
    reverse_comp=trans.upper()
    return reverse_comp
    
def test_lower():
    expected='ATCG'
    observed=rev_comp('cgat')
    assert observed == expected, f'expected {expected}, got {observed}'

def test_upper():
    expected='ATCG'
    observed=rev_comp('CGAT')
    assert observed == expected, f'expected {expected}, got {observed}'

def test_mixed():
    expected='ATCG'
    observed=rev_comp('cGaT')
    assert observed == expected, f'expected {expected}, got {observed}'

def test_non():
    try:
        observed=rev_comp('ATXCG')
    except TypeError:
        return
    assert False, f'expected TypeError exception, got ({observed})'
    