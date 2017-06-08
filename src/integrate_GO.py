import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
class GO:
	def __init__(self, FILE="../files/goa_human.csv"):
		self.f 	= FILE
		self.G 	= defaultdict(list)
		self._load()
	def _load(self):
		self.df 	= pd.read_csv(self.f)
		for x,y in zip(self.df.gene,self.df.GOid):
			self.G[x].append(y)
	def get_associated_go_terms(self, INPUT):
		return [self.G[i] if i in self.G else [] for i in INPUT]


if __name__=="__main__":
	g 	= GO()