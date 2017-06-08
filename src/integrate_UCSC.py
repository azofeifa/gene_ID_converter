import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

class UCSC:
	def __init__(self, FILE="../files/RefSeqHG19.tsv"):
		self.f 			= FILE
		self.lengths 	= defaultdict(list)
		self._load()
	def _load(self):
		self.df 	= pd.read_csv(self.f,sep="\t")
		for x,y in zip(self.df.name2,np.abs(self.df.txStart-self.df.txEnd)):
			self.lengths[x].append(y)
		self.lengths 	= dict([(x, np.mean(self.lengths[x]) )for x in self.lengths])
	def get_associated_lengths(self, INPUT):
		return [self.lengths[i] if i in self.lengths else float("nan") for i in INPUT]
		

if __name__=="__main__":
	g 	= UCSC()