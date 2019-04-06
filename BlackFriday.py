#veri ve analizi için 
import pandas as pd 
import numpy as np
#Goruntuleme icin
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("BlackFriday.csv")
print(df.info())
print(df.shape)


#%% kayıp veriler
#karşılığı null olan verileri sayip toplamını buluyoruz
toplamKayip=df.isnull().sum()
#kaybettiğimiz toplam verileri bulduk ve yüzde cinsinde ifade ettik
yuzde_cinsinden_kayip=toplamKayip/df.isnull().count()*100
#kaybettiğimiz toplam verileri buluyoruz
kayip_veri=pd.DataFrame({'Toplam Kayip':toplamKayip,
                         '% kayip':yuzde_cinsinden_kayip})
#katbettiğimiz toplam verileri büyükten küçüğe sıraladık ilk üçünü bastık
kayip_veri.sort_values(by='Toplam Kayip',ascending=False).head(3)


#%% Eşsiz veriler
print("Her Özellik için Benzersiz Değerler")
#özellikle essiz verileri bulduk
for i in df.columns:
    print(i,":",df[i].nunique())
    
#%%Ürünler Hakkında Bilgi
print("Toplam Urun Sayisi:",df['Product_ID'].nunique())    
print("Kategori Sayisi: ",df['Product_Category_1'].unique().max())
print("En yuksek ve en dusuk satin alma :",df['Purchase'].max(),',',df['Purchase'].min())


#%%Müsteriler hakkında Bilgi
print("Musteri Sayisi :",df['User_ID'].nunique())
print("Sehirdeki yıl sayisi :",df['Stay_In_Current_City_Years'].unique())
print("Yaş Grupları :",df['Age'].unique())

#%%Cinsiyetler
e_sayisi=df[df['Gender']=='M'].count()[0]
k_sayisi=df[df['Gender']=='F'].count()[0]

print("Toplam erkek sayisi : ",e_sayisi)
print("Toplam kadin sayisi : ",k_sayisi)

"""
Musteri sayilarinda erkek sayisinin kadin sayisinden
fazla olduğunu gördük. Bu nedenle kayitları saymak yerine
oranlara gore cinsiyet analizi yapmak daha Bilgilendirici olucaktır
Her bir cinsiyetin kendine göre ne kadar harcadıklarını bulalım
"""
print("Kadın harcamaları :",round(df[df['Gender']=='F']['Purchase'].sum()/k_sayisi,2))
# round metotu round(icerik,virgulden sonra kaç basamak gelicek)
print("Erkek harcamaları :",round(df[df['Gender']=='M']['Purchase'].sum()/e_sayisi,2))
#%% pasta grafik çıkarma 
plt.pie(df.groupby('Gender')['Product_ID'].nunique(),labels=['Male','Famele'],shadow=True,colors=['steelblue','pink'],autopct='%1.1f%%')
plt.title("Cinsiyete Gore Essiz Urun alımları")
plt.show()


