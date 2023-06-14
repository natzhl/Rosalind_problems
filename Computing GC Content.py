from Bio import SeqIO

fasta_sequences = SeqIO.parse(('/content/rosalind_gc.txt'),'fasta')

id = []
seq = []

for fasta in fasta_sequences: 
  id.append(fasta.id)
  seq.append(str(fasta.seq)) 

def computing_GC(seq):
  return((seq.count('C') + seq.count('G')) / len(seq)) * 100

computing_GC_list = [] # list for all GC sums

for fasta in seq:
  computing_GC_list.append(computing_GC(fasta))

print(max(computing_GC_list))
max_index = computing_GC_list.index(max(computing_GC_list))
print(id[max_index])
