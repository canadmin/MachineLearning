#mesela en zengin ve en fakir insanlar nerelerde guruplanmışlar 


import numpy as np


def createClusteredData(N,k):
    np.random.seed(10)
    pointsPerCluster=float(N)/k
    x=[]
    for i in range(k):
        incomeCentroid=np.random.uniform(20000.0,200000.0)
        ageCentroid=np.random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,2.0)])
    x=np.array(x)
    return x

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale #verileri normalize etmek için

data = createClusteredData(100,5)
model = KMeans(n_clusters=5)

scaledData=scale(data)
model=model.fit(scaledData)
print(model.labels_)

plt.figure(figsize=(8,6))
plt.scatter(data[:,0],data[:,1],c=model.labels_.astype(float))

