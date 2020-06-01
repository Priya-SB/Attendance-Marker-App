# -*- coding: utf-8 -*-

import re
import pandas as pd
import operator

class Extractor():
    def __init__(self, dates, zoomfile, classfile):
        self.class_df=self.load_file(classfile, dates)
        self.zoom_dist1=self.build_ngram_1(zoomfile)
        self.zoom_dist2=self.build_ngram_2(zoomfile)
        self.zoom_dist3=self.build_ngram_3(zoomfile)
        self.table=[]
        self.outFile=classfile
    
    def load_file(self, filename, col):
        df=pd.read_excel(filename)
        df=df.iloc[:-1,:]
        df[col]=[0]*len(df)
        return df
        
    def build_ngram_1(self, filename):
        dist={}
        dist.update(self.parse_file(filename, 1))
        return dist
    
    def build_ngram_2(self, filename):
        dist={}
        dist.update(self.parse_file(filename, 2))
        return dist
    
    def build_ngram_3(self, filename):
        dist={}
        dist.update(self.parse_file(filename, 3))
        return dist
    
    def parse_file(self,filename,n):
        f=open(filename,'r')
        results={}
        for line in f:
            words=self.clean_phrase(line).split(" ")
            ngrams=self.ngrams(words,n)
            for tup in ngrams:
                phrase=" ".join(tup)
                if phrase in results.keys():
                    results[phrase]+=1
                else:
                    results[phrase]=1
        return results
    
    def clean_phrase(self,line):
        line=line.replace(')',' ').replace(']',' ').replace('(',' ').replace('[',' ').replace('}',' ').replace('{',' ')
        return re.sub(r'[^\w\s]','',line.replace('\n',' ').replace('\t',' ').lower())
    
    def ngrams(self,input_list, n):
        return list(zip(*[input_list[i:] for i in range(n)]))
    
    def sendToFile(self):
        self.class_df.to_excel(self.outFile,index=False)
        
    def makeTable(self, dates):
        
        lang1 = sorted(self.zoom_dist1.items(), key=operator.itemgetter(1),reverse=True)
        lang2 = sorted(self.zoom_dist2.items(), key=operator.itemgetter(1),reverse=True)
        lang3 = sorted(self.zoom_dist3.items(), key=operator.itemgetter(1),reverse=True)
        
        for i in range(len(self.class_df)):
            roll=self.clean_phrase(self.class_df.iloc[i,1])
            prn=str(self.class_df.iloc[i,2])
            val=self.clean_phrase(self.class_df.iloc[i,3])
            
            if len(roll)==3:
                roll1=roll[:2]+'0'+roll[2:]
            else:
                roll1=roll
            
            for tuple in lang1:
                item = tuple[0]
                if item == roll1 or item == prn or item == val:
                    self.class_df.iloc[i,-1]=1
                
            for tuple in lang2:
                ite = tuple[0]
                if ite == val:
                    self.class_df.iloc[i,-1]=1
                    
                tup=tuple[0].replace(" ",'')
                if tup == roll1:
                    self.class_df.iloc[i,-1]=1
                    
            for tuple in lang3:
                ite = tuple[0]
                if ite == val:
                    self.class_df.iloc[i,-1]=1

        self.class_df.loc[-1,4:]= self.class_df.iloc[:-1,4:].sum(numeric_only=True, axis=0)
        self.sendToFile()
#------------------------------------------------------------------------------

def main(dates, zoomfile, classfile):
    K=Extractor(dates, zoomfile, classfile)
    K.makeTable(dates)
    K.sendToFile()

if __name__ == "__main__":
    main()