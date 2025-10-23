#!/usr/bin/env
import pytest
def gc_content(seq):
    upper=seq.upper()
    valid = {'A', 'C', 'G', 'T'}
    if not set(upper).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(upper) == 0:
        return 0
    return (upper.count('G') + upper.count('C')) / len(upper)

def test_gccontent():
    expected= 0.25
    observed = gc_content('gattacaa')
    assert observed == expected, f'expected {expected}, got {observed}'
    

def test_accontent():
    expected = 0.0
    observed = gc_content('ATAT')
    assert observed == expected, f'expected {expected}, got {observed}'

def test_ATGC():
    expected = 0.5
    observed = gc_content('ATGC')
    assert observed == expected, f'expected {expected}, got {observed}'

def test_ATGXB():
    try:
        observed = gc_content('ATGXB')
    except TypeError:
        return
    assert False, f'expected TypeError exception, got ({observed})'




