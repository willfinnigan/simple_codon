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
