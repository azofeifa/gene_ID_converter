'''
	the most glorious website, gene name tool thing, ever

	http://www.genenames.org/cgi-bin/download

'''
import pandas as pd
import time
class db:
	def __init__(self, table="../files/HUGO_table.tsv"):
		self.df 	= pd.read_csv(table,sep="\t")
		'''make dictionaries for faster look ups
		'''
	def _ensembl(self):
		print "making ensembl ID structure (->common)...",
		self.E_common 	= dict([(row["Ensembl Gene ID"], row["Approved Symbol"]) for i,row in self.df.iterrows() ])
		print "done"
	def _refseq(self):
		print "making ensembl ID structure (->refseq)...",
		self.E_refseq 	= dict([(row["Ensembl Gene ID"], row["RefSeq IDs"]) for i,row in self.df.iterrows() ])
		print "done"
	def from_ensembl_to_common(self, ensembl):
		if not hasattr(self, "E_common"):
			self._ensembl()
		if ensembl not in self.E_common:
			return "NaN"
		return self.E_common[ensembl]
	def from_ensembl_to_refseq(self, ensembl):
		if not hasattr(self, "E_refseq"):
			self._refseq()
		if ensembl not in self.E_refseq:
			return "NaN"
		return self.E_refseq[ensembl]


def main():
	f 	= "/Volumes/Joeys_External/BBC/FORMA/TCGA_DATA_3/64089c20-939f-48b4-ae8b-904ad0597145/98921931-2f32-470d-97ae-824716d1c034.FPKM.txt"
	T 	= pd.read_csv(f,sep="\t",header=None)
	DB = db()
	st = time.clock()
	g 	= map(DB.from_ensembl_to_refseq, T[0])

if __name__ == "__main__":
	main()