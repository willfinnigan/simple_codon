# simple_codon

## Description
a simple function for codon optimisation

The function `make_new_seq(protein_seq, codon_table, low_cuttoff)` found in optimisation_function.py is used
This will return a dna_sequence


## Example
To make a codon optimised dna sequence, use the function make_new_seq
'dna_seq = make_new_seq(protein_seq, codon_table, low_cuttoff)'  

There are three arguments: 

protein_seq - this should be a protein that looks like the following:  
`protein = "MRAVVFENKERVAVKEVNAPRLQHPLDALVRVHLAGICGSDLHLYHGKIPVLPGSVLGHEFVGQVEAVGEGIQDLQPGDWVVGPFHIACGTCPYCRRHQYNLCERGGVYGYAIPINAEQENP*"`

codon_table - this should be a dictionary that looks like the following:  
```
codon_table = {  
        "A": {"GCT": 24, "GCG": 227, "GCC": 733, "GCA": 17},  
        "R": {"AGA": 10, "CGA": 15, "CGT": 19, "AGG": 189, "CGC": 340, "CGG": 426},  
        "N": {"AAT": 27, "AAC": 973},  
        "D": {"GAT": 48, "GAC": 952},  
        "C": {"TGT": 50, "TGC": 950},  
        "*": {"TAA": 195, "TAG": 368, "TGA": 438},  
        "Q": {"CAA": 130, "CAG": 870},  
        "E": {"GAA": 125, "GAG": 875},  
        "G": {"GGT": 25, "GGA": 61, "GGC": 400, "GGG": 515},  
        "H": {"CAT": 50, "CAC": 950},  
        "I": {"ATA": 46, "ATT": 94, "ATC": 860},  
        "L": {"TTA": 8, "CTA": 22, "TTG": 66, "CTT": 114, "CTG": 285, "CTC": 505},  
        "K": {"AAA": 85, "AAG": 915},  
        "M": {"ATG": 1000},  
        "F": {"TTT": 177, "TTC": 823},  
        "P": {"CCA": 23, "CCT": 68, "CCG": 176, "CCC": 733},  
        "S": {"TCA": 9, "AGT": 11, "TCT": 24, "TCG": 110, "AGC": 399, "TCC": 446},  
        "T": {"ACA": 11, "ACT": 12, "ACG": 250, "ACC": 726},  
        "W": {"TGG": 1000},  
        "Y": {"TAT": 43, "TAC": 957},  
        "V": {"GTA": 17, "GTT": 31, "GTC": 336, "GTG": 615}}  
```
And a low_cuttoff.  This is the frequency below which triplets will not be used.  
In this example frequencies for each amino acid total 1000, 
so a cuttoff of 100 removes codons used less than 10% of the time  
`codon_cuttoff = 100`

Make an individual sequence and print  
`new_seq = make_new_seq(protein, codon_table, codon_cuttoff)`

`print(new_seq)`  
`> ATGCGCGCCGTGGTCTTCGAGAACAAGGAGCGGGTGGCGGTCAAGGAGGTGAACGCGCCCCGGCTGCAACACCCCCTCGACGCCCTTGTGCGCGTCCACCTTGCCGGGATCTGCGG  
GAGCGACCTGCACCTCTACCACGGCAAGATCCCCGTCCTGCCCGGGTCCGTCCTCGGCCACGAGTTCGTGGGGCAGGTGGAGGCCGTCGGGGAGGGGATCCAGGACCTCCAGCCGGGGG  
ACTGGGTGGTGGGGCCCTTCCACATCGCCTGCGGCACGTGCCCCTACTGCCGGCGCCACCAATACAACCTCTGCGAGCGGGGGGGGGTGTACGGCTACGCCATCCCGATCAACGCCGAG  
CAGGAGAACCCGTGA`

