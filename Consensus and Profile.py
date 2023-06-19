from Bio import SeqIO
import numpy as np

fasta_sequences = SeqIO.parse(('/content/rosalind_cons (6).txt'),'fasta')

id = []
seq = []

for fasta in fasta_sequences:
  id.append(fasta.id)
  seq.append(str(fasta.seq))

def profile_and_consensus(seq):
  n = len(seq[0])
  profile_matrix = {
      'A': [0] * n,
      'C': [0] * n,
      'G': [0] * n,
      'T': [0] * n
  }
  for row in seq:
    for position, elem in enumerate(row): 
      if elem == 'A':
        profile_matrix[elem][position] += 1
      elif elem == 'C':
        profile_matrix[elem][position] += 1
      elif elem == 'G':
        profile_matrix[elem][position] += 1
      elif elem == 'T':
        profile_matrix[elem][position] += 1
  profile_matrix_result = [print(i+':',*profile_matrix[i]) for i in profile_matrix]

  consensus = []
  for position in range(n):
    max_count = 0
    max_nucleotide = None
    for elem in profile_matrix:
      count = profile_matrix[elem][position]
      if count > max_count:
          max_count = count
          max_nucleotide = elem
    consensus.append(max_nucleotide)
  consensus = ''.join(consensus)

  return profile_matrix_result, consensus

profile_and_consensus(seq)
