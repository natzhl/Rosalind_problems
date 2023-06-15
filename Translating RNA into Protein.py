codon_table = {'F': ['UUU', 'UUC'],
               'L': ['CUU', 'CUC', 'UUA', 'UUG', 'CUA', 'CUG'],
               'I': ['AUU', 'AUC', 'AUA'],
               'V': ['GUC', 'GUA', 'GUG', 'GUU'], 
               'M': ['AUG'],
               'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
               'P': ['CCU', 'CCC', 'CCA', 'CCG'],
               'T': ['ACU', 'ACC', 'ACA', 'ACG'],
               'A': ['GCU', 'GCC', 'GCA', 'GCG'],
               'Y': ['UAU', 'UAC'],
               'H': ['CAU', 'CAC'],
               'N': ['AAU', 'AAC'],
               'D': ['GAU', 'GAC'],
               'Q': ['CAA', 'CAG'],
               'K': ['AAA', 'AAG'],
               'E': ['GAA', 'GAG'],
               'C': ['UGU', 'UGC'],
               'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
               'G': ['GGU', 'GGC', 'GGA', 'GGG'],
               'W': ['UGG'],
               'Stop': ['UAA', 'UAG', 'UGA']}

def translating(str):
  n = 3
  triplets = [str[i:i+n] for i in range(0, len(str), n)]
  for i in triplets:
    for key, value in codon_table.items():
        if i in value:
            print(key, end="")
  return key
