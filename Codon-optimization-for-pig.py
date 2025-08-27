
optimal_codons = {
    'A': 'GCC',
    'C': 'TGC',
    'D': 'GAC',
    'E': 'GAG',
    'F': 'TTC',
    'G': 'GGC',
    'H': 'CAC',
    'I': 'ATC',
    'K': 'AAG',
    'L': 'CTG',
    'M': 'ATG',
    'N': 'AAC',
    'P': 'CCC',
    'Q': 'CAG',
    'R': 'CGC',
    'S': 'TCC',  # TCC selected over AGC due to slightly higher frequency/1000 (18.6 vs 18.3)
    'T': 'ACC',
    'V': 'GTG',
    'W': 'TGG',
    'Y': 'TAC',
    '*': 'TGA'   # Highest frequency stop codon
}

def optimize_for_pig(protein_seq):
    """
    Takes a protein sequence (string of single-letter amino acids), converts it to an optimized mRNA sequence
    using the highest frequency codons for pig, appends the optimal stop codon, and then converts to DNA sequence.
    
    Assumes input is uppercase and valid; does not handle errors.
    """
    # Build mRNA sequence (with U)
    mrna_seq = ''.join(optimal_codons[aa].replace('T', 'U') for aa in protein_seq)
    # Add stop codon
    stop_codon = optimal_codons['*'].replace('T', 'U')
    mrna_seq += stop_codon
    
    # Convert to DNA (replace U with T)
    dna_seq = mrna_seq.replace('U', 'T')
    
    return mrna_seq, dna_seq

# Example usage as a script
if __name__ == "__main__":
    protein_sequence = input("Enter the protein sequence: ").strip().upper()
    mrna, dna = optimize_for_pig(protein_sequence)
    print("\nOptimized mRNA sequence:")
    print(mrna)
    print("\nOptimized DNA sequence (gene):")
    print(dna)

