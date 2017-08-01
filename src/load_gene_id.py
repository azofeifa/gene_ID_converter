'''
	the most glorious website, gene name tool thing, ever

	http://www.genenames.org/cgi-bin/download

'''
import pandas as pd
import time,numpy as np,sys
import os
PATH 	= "/".join(os.path.realpath(__file__).split("/")[:-2])
class db:
	def __init__(self, table=PATH+"/files/HUGO_table.tsv",verbose=False):
		self.df 	= pd.read_csv(table,sep="\t")
		'''make dictionaries for faster look ups
		'''
		self.verbose 			= verbose
		self._make_relational_dictionaries()
	def _make_relational_dictionaries(self):
		st 		= time.clock()
		self.V,self.E,self.R,self.AR 	= dict(),dict(),dict(),dict()
		if self.verbose:
			print "making data structures...",;sys.stdout.flush();
		for i,row in self.df.iterrows():
			self.V[str(row["Vega ID"]).lower()],self.E[str(row["Ensembl Gene ID"]).lower()],self.R[str(row["RefSeq IDs"]).lower()] 	= i,i,i
			self.AR[str(row["Approved Symbol"]).lower()] 	= i
		if self.verbose:
			print "done (" + str(time.clock()-st)[:4] + " seconds)";sys.stdout.flush(); 
	def _grab(self, a):
		a 	= a.lower()
		if a in self.E:
			return str(self.df.loc[self.E[a]][self.column]).upper()
		if a in self.V:
			return str(self.df.loc[self.V[a]][self.column]).title()
		if a in self.R:
			return str(self.df.loc[self.R[a]][self.column]).title()
		return "nan"
	def mapToEnsembl(self, args):
		st,vs = time.clock(),list()
		if self.verbose:
			print "\nmapping input IDS...",;sys.stdout.flush();
		for a in args:
			a 	= a.lower()
			if a in self.E:
				vs.append(a.upper())
			elif a in self.AR:
				idx 	= self.AR[a]
				vs.append(self.df.iloc[idx]["Ensembl Gene ID"])
			else:
				vs.append("nan")

		vs = np.array(vs)
		if self.verbose:
			print "done (" + str(time.clock()-st)[:4] + " seconds)\n" 
			if len(vs):
				print "I was able to map",sum(vs!="nan"), "/",len(vs), "of your IDS\n"
				print "I couldn't map: " + ",".join([args[i] for i,v in enumerate(vs) if v == "nan"])
			else:
				print "I wasn't able to map any of your IDS\n"
		return np.array(vs)
	def map(self, args,out="Approved Symbol"):
		st,self.column	= time.clock(), out
		if self.verbose:
			print "mapping input IDS...",;sys.stdout.flush();
		vs 				= np.array(map(self._grab, [a.split(".")[0] for a in args] ))
		if self.verbose:
			print "done (" + str(time.clock()-st)[:4] + " seconds)\n" 
			print "I was able to map",sum(vs!="nan"), "/",len(vs), "of your IDS\n"
		return vs

def main():
	f 	= "/Volumes/Joeys_External/BBC/FORMA/TCGA_DATA_3/64089c20-939f-48b4-ae8b-904ad0597145/98921931-2f32-470d-97ae-824716d1c034.FPKM.txt"
	T 	= pd.read_csv(f,sep="\t",header=None)
	DB = db()
	st = time.clock()
	vs = DB.map(T[0])
if __name__ == "__main__":
	main()