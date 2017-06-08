'''
	the most glorious website, gene name tool thing, ever

	http://www.genenames.org/cgi-bin/download

'''
import pandas as pd
import time,numpy as np,sys
import os
PATH 	= "/".join(os.path.realpath(__file__).split("/")[:-2])
class db:
	def __init__(self, table=PATH+"/files/HUGO_table.tsv"):
		self.df 	= pd.read_csv(table,sep="\t")
		'''make dictionaries for faster look ups
		'''
		self._make_relational_dictionaries()
	def _make_relational_dictionaries(self):
		st 		= time.clock()
		self.V,self.E,self.R 	= dict(),dict(),dict()
		print "making data structures...",;sys.stdout.flush();
		for i,row in self.df.iterrows():
			self.V[row["Vega ID"]],self.E[row["Ensembl Gene ID"]],self.R[row["RefSeq IDs"]] 	= i,i,i
		print "done (" + str(time.clock()-st)[:4] + " seconds)";sys.stdout.flush(); 
	def _grab(self, a):

		if a in self.E:
			return str(self.df.loc[self.E[a]][self.column])
		if a in self.V:
			return str(self.df.loc[self.V[a]][self.column])
		if a in self.R:
			return str(self.df.loc[self.R[a]][self.column])
		return "NaN"

	def map(self, args,out="Approved Symbol"):
		st,self.column	= time.clock(), out
		print "mapping input IDS...",;sys.stdout.flush();
		vs 				= np.array(map(self._grab, [a.split(".")[0] for a in args] ))
		print "done (" + str(time.clock()-st)[:4] + " seconds)\n" 
		print "I was able to map",sum(vs!="NaN"), "/",len(vs), "of your IDS\n"
		return vs

def main():
	f 	= "/Volumes/Joeys_External/BBC/FORMA/TCGA_DATA_3/64089c20-939f-48b4-ae8b-904ad0597145/98921931-2f32-470d-97ae-824716d1c034.FPKM.txt"
	T 	= pd.read_csv(f,sep="\t",header=None)
	DB = db()
	st = time.clock()
	vs = DB.map(T[0])
if __name__ == "__main__":
	main()