def to_rna(dna_strand):
    rna_strand: str = ""
    for chr in dna_strand:
        if chr == "A":
            rna_strand += "U"
        elif chr == "T":
            rna_strand += "A"
        elif chr == "C":
            rna_strand += "G"
        elif chr == "G":
            rna_strand += "C"
    return rna_strand


print(to_rna("AGGGCA"))