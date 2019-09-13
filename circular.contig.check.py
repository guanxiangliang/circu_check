#! python3
'''
$ python circular.contig.py  original.fasta
'''

from Bio import SeqIO
import sys

print("contig.id"+"\t"+"length"+"\t"+"circularity")
for contig in  SeqIO.parse(open(sys.argv[1]), 'fasta'):

	length = len(contig.seq)

	if length < 500: 
		print(contig.id +"\t"+ str(length)+"\t"+"short")
	else:
		for k in range(10,1001):
			if contig.seq[0:k] == contig.seq[length-k:]:
				print(contig.id+"\t"+str(length)+"\t"+"circular")
				exit()
		print(contig.id+"\t"+str(length)+"\t"+"non-circular")
