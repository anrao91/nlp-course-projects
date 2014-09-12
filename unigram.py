import nltk
import csv
from collections import defaultdict
import re
from math import log

words = nltk.word_tokenize(open("corpus2.txt").read().lower())
vwords = defaultdict(int)

punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&' ]
count = 0

for word in words:
	if(not word in punctuation):
		word = re.sub(r'[,.\']','',word)
		vwords[word] += 1
		count += 1
maxl=len(max(vwords,key=len))
#highest=max(vwords,key=len)
#print highest
csvfile="unigram2.csv"
with open(csvfile,"w") as output:
    writer = csv.writer(output,lineterminator="\n")
    for key,value in vwords.iteritems():
        probab = (1.0*value)/count
        writer.writerow(key+"".ljust(maxl-len(key))+","+str(probab)+","+str(log(probab)))


