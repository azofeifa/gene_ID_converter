'''make gene ID meta file for RNASeek
'''
from load import db
from integrate_GO import GO
from integrate_UCSC import UCSC
import math

def main():
	HUGO 		= db()
	go 		= GO()	
	ucsc 		= UCSC()
	ensmbl 	= map(str, HUGO.E.keys())
	common 	= HUGO.map(ensmbl)
	go_terms = go.get_associated_go_terms(common)
	lengths 	= ucsc.get_associated_lengths(common)
	gos_all 	= set([i for x in go_terms for i in x])
	FHW 		= open("../files/gene_id_table.csv","w")
	FHW.write("gene,length,go_id"+ "\n" )

	for i,g in enumerate(ensmbl):
		gos 	= set(go_terms[i])
		for go in gos:
			try:
				FHW.write(g + ","+ go +","+str(int(lengths[i])) + "\n")
			except:
				pass



if __name__ == "__main__":
	main()