# the lea library makes it easy to make a weighted random choice from a dictionary
import lea

def make_new_seq(protein_seq, codon_table, low_cuttoff):
    """
    This function takes a protein_sequence in the form MGACREDATY...,
    a codon table in the form {"N": {"AAT": 27, "AAC": 973}, "D": {"GAT": 48, "GAC": 952},...}
    and a low_cuttoff below which triplets will not be picked  (eg 100)

    A dna sequence will be returned for the protein,
    with codon bias similar to the provided codon table,
    but avoiding any triplets with frequencies below the low cuttoff
    """

    # make an empty variable to hold the new dna sequence
    dna_seq = ""

    # iterate through the protein sequence
    for aminoacid in protein_seq:

        # loop this section until a triplet which has a higher frequency than the low cuttoff is selected
        triplet_selected = False
        while triplet_selected == False:

            # get the dict of triplets for this amino acid
            # this will look like {"AAT": 27, "AAC": 973}
            codon_dict = codon_table.get(aminoacid)

            # make an lea dictionary from codon_dict
            # the lea library makes it easy to do weighted random selection
            lea_codon_dict = lea.Lea.fromValFreqsDict(codon_dict)

            # select a triplet randomly, weighted by the frequency of occurance
            triplet = lea_codon_dict.random()

            # if the triplet selected has a higher frequency than the cuttoff,
            # add the triplet to dna_seq and finish the while loop
            if codon_dict.get(triplet) > low_cuttoff:
                triplet_selected = True
                dna_seq += triplet

    # having iterated through the protein sequence, dna_seq is complete
    return dna_seq
