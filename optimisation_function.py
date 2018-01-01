import lea

def make_new_seq(protein_seq, codon_table, low_cuttoff):

    dna_seq = ""

    for i in range(len(protein_seq)):
        codon_selected = False
        while codon_selected == False:
            aminoacid = protein_seq[i]
            codon_dict = codon_table.get(aminoacid)
            lea_codon_dict = lea.Lea.fromValFreqsDict(codon_dict)
            codon = lea_codon_dict.random()

            if codon_dict.get(codon) > low_cuttoff:
                codon_selected = True
                dna_seq += codon

    return dna_seq


if __name__ == "__main__":
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

    # Protein sequence and low cuttoff for testing...
    protein = "MRAVVFENKERVAVKEVNAPRLQHPLDALVRVHLAGICGSDLHLYHGKIPVLPGSVLGHEFVGQVEAVGEGIQDLQPGDWVVGPFHIACGTCPYCRRHQYNLCERGGVYGYGPMFGNLQGAQAEILRVPFSNVNLRKLPPNLSPERAIFAGDILSTAYGGLIQGQLRPGDSVAVIGAGPVGLMAIEVAQVLGASKILAIDRIPERLERAASLGAIPINAEQENPVRRVRSETNDEGPDLVLEAVGGAATLSLALEMVRPGGRVSAVGVDNAPSFPFPLASGLVKDLTFRIGLANVHLYIDAVLALLASGRLQPERIVSHYLPLEEAPRGYELFDRKEALKVLLVVRGGGSGDYKDDDDK**"

    codon_cuttoff = 100

    # Make an individual sequence and print
    new_seq = make_new_seq(protein, codon_table, codon_cuttoff)

    print(new_seq)