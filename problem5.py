def dna_transcriber(dna_sequence, codon_table):
    if len(dna_sequence)%3 != 0:
        return False
    new_list = []
    copy_of_sequence = dna_sequence[:]
    while copy_of_sequence:
        chunk = copy_of_sequence[:3]
        if chunk in codon_table:
            new_list.append(codon_table[chunk])
        copy_of_sequence = copy_of_sequence[3:]
    new_string = '-'.join(new_list)
    print(f"\nSequence: {dna_sequence}")
    print(f"Proteins: {new_string}\n")
    

codon_table = {
    "ATG": "Methionine",
    "GCG": "Alanine",
    "TCC": "Serine",
    "TAT": "Tyrosine",
    "CGT": "Arginine"
}
dna_sequence = "ATGCGTTATGCG"
dna_transcriber(dna_sequence, codon_table)