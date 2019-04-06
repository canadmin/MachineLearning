import pandas as df #movilens veri seti
r_columns=['user_id','movie_id',"rating"]

ratings=df.read_csv('u.data',sep="\t",names=r_columns,usecols=range(3))

m_columns=["movie_id","title"]

movies=df.read_csv("u.item",sep="|",names=m_columns,usecols=range(2),
                   encoding="latin-1")

ratings2=df.merge(movies,ratings)

user_ratings=ratings2.pivot_table(index="user_id",columns="title",values="rating")
starWarsRatings=user_ratings['Star Wars (1977)']
benzerFilmler=user_ratings.corrwith(starWarsRatings)
benzerFilmler=benzerFilmler.dropna()
df1=df.DataFrame(benzerFilmler)

import numpy as np
filmistatistik=ratings2.groupby("title").agg({
        'rating':[np.size,np.mean]})


populerFilmler=filmistatistik['rating']['size']>=100
sonuc=filmistatistik[populerFilmler].sort_values([('rating','mean')],ascending=False)[:15]
