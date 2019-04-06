from pandas import DataFrame
import os as o
import io as i
from sklearn.feature_extraction.text import CountVectorizer#metin içindeki kelimelerin frakasları ile vektor olusturuyor
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirNames,fileNames in o.walk(path):
        for fileName in fileNames:
            path=o.path.join(root,fileName)
            inBody=False
            lines=[]
            f=i.open(path,'r',encoding="latin1")
            for line in f:
                if inBody:
                    lines.append(line)
                elif line=="\n":
                     inBody=True
            f.close()
            message="\n".join(lines)
            yield path,message
            
          
def createdataFrame(path,classification):
    rows=[]
    index=[]
    for fileName,message in readFiles(path):
        rows.append({"message":message,'class':classification})
        index.append(fileName)
        
    return DataFrame(rows,index=index)

data=DataFrame({'message':[],'class':[]})
data=data.append(createdataFrame("spam",'spam'))
data=data.append(createdataFrame("ham",'ham'))

vectorizer=CountVectorizer()

counts=vectorizer.fit_transform(data["message"].values)        
model=MultinomialNB()
target=data['class'].values
model.fit(counts,target)#giris cıkıs
            
example=["CLICK HERE to Order Yours NOW!",
         "Hi bob How about a game of golf tomarrow"] 
example_counts=vectorizer.transform(example)           
tahmin=model.predict(example_counts)