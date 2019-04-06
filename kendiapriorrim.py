import pandas as pd

df=pd.read_csv("sepetanalizi.csv",sep=";")
df=df.dropna()
sutun_isimleri=list(df.head(0))
yeniSutunİsimleri=[]
satilan_urun_sayisi=df.iloc[:,1]

musterisayi=len(satilan_urun_sayisi)

sozluk={}

for i in range(1,len(sutun_isimleri)):
    yeniSutunİsimleri.append(sutun_isimleri[i])
yeniListeSatilan=[]
toplam=0
for i in range(1,len(sutun_isimleri)):
    satilan_urun_sayisi=df.iloc[:,i]
    for j in range(len(satilan_urun_sayisi)):
        if(satilan_urun_sayisi[j]=="evet"):
            toplam+=1        
    yeniListeSatilan.append(toplam)
    toplam=0 
for i in range(len(yeniListeSatilan)):
        sozluk[yeniSutunİsimleri[i]]=yeniListeSatilan[i]
        
destek_orani=[]
for i in range(len(yeniListeSatilan)):
    sonuc=yeniListeSatilan[i]/musterisayi
    destek_orani.append(sonuc*100)
    
destek_orani_v2=[]
urun_listesi_v2=[]
sozluk2={}

for i in range(len(destek_orani)):
    if(destek_orani[i]>25.0):
        destek_orani_v2.append(destek_orani[i])
        urun_listesi_v2.append(yeniSutunİsimleri[i])
        sozluk2[yeniSutunİsimleri[i]]=[destek_orani[i]]
        
urun_listesi_ikili=[]
sepetlistesi={}
df2=pd.read_csv("sepetanalizi.csv",sep=";",usecols=urun_listesi_v2)
df2=df2.dropna()
#%%
for i in range(0,musterisayi):
    satir=df2.iloc[i,:]
    for j in range(len(satir)):
        if(satir[j]=="evet"):
            urun_listesi_ikili.append(urun_listesi_v2[j])
    sepetlistesi[i]=urun_listesi_ikili
    urun_listesi_ikili=[]
#%%
counterİkili=[]
virgulluİkili=[]
isima1=[]
isima2=[]

#%%
for i in range(0,len(urun_listesi_v2)):
      for j in range(i,len(urun_listesi_v2)):
          if(i!=j):
            isim1=urun_listesi_v2[i]
            isim2=urun_listesi_v2[j]
            counterİkili.append(isim1+" "+isim2)
            virgulluİkili.append(isim1+","+isim2)
            isima1.append(isim1)
            isima2.append(isim2)
      i=j    
#%%
counter=0 
eslestir=[]
destek_orani_ikili=[]
yeniCounterİkili=[]
yeniVirgulluİkili=[]
for i in range(0,len(counterİkili)):
       for j in range(0,len(sepetlistesi)):
           dlist=sepetlistesi.get(j) 
           if(isima1[i] in dlist and isima2[i] in dlist):
               counter+=1
       eslestir.append(counter) 
       counter=0
       
sozluk3={}       
for i in range(0,len(counterİkili)):
    a=eslestir[i]/musterisayi*100
    if(a>=25):
        destek_orani_ikili.append(a)
        yeniVirgulluİkili.append(virgulluİkili[i])
        yeniCounterİkili.append(counterİkili[i])
        sozluk3[counterİkili[i]]=a
        
        
#%%
counter=0
sonListe=[]
for i in range(0,len(yeniVirgulluİkili)):
        parseEt=yeniVirgulluİkili[i].split(",")
        for j in range(len(parseEt)):
            if(parseEt[j] not in sonListe):
                sonListe.append(parseEt[j])
        
        
        
 #%%yeni bir üçlü liste oluşacak
 
ucluSonListe=[]
for i in range(0,len(yeniVirgulluİkili)):
        parseEt=yeniVirgulluİkili[i].split(",")
        ucuncuUrun=sonListe[i]
        if(ucuncuUrun!=parseEt[0] and ucuncuUrun!=parseEt[1]):
            eleman=parseEt[0]+","+parseEt[1]+","+ucuncuUrun
            ucluSonListe.append(eleman)
            
#%% yukarida üçlü olarak hazırladıktan sonra tekrar bakıcaz
#%% son fonksiyon kaldı buraya üclü göndericez sonra biticek   
       

