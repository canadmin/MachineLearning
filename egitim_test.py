import numpy as np
import matplotlib.pyplot as plt


sayfaHizi = np.random.normal(3.0,1.0,100)
satisToplami = np.random.normal(50.0,30.0,100)
plt.scatter(sayfaHizi,satisToplami)
trainX = sayfaHizi[:80]
trainY = satisToplami[:80]
# Eğitim verileri oluşturuldu

testX = sayfaHizi[80:]
testY = satisToplami[80:]
# test verileri oluşturuldu

plt.scatter(trainX,trainY)
# eğitim verilerine göre grafik çizildi.

plt.scatter(testX,testY)
# test verilerine göre grafik çizildi.

x = np.array(trainX)
y = np.array(trainY)
# polinominal regresyon oluşturduk.

testx = np.array(testX)
testy = np.array(testY)
plt.scatter(testX,testY,c='g')



# oluşturulan polinaminal grafiğe göre test verileri oluşturul

pol = np.poly1d(np.polyfit(x,y,8))
veri = np.linspace(0,7,100)
axes = plt.axes()
axes.set_xlim(0,7)
axes.set_ylim(0,200)
plt.scatter(x,y)
plt.plot(veri, pol(veri),c='r')



plt.show()
from sklearn.metrics import r2_score
print(r2_score(testy,pol(testx)))
r2_score(y,pol(x))