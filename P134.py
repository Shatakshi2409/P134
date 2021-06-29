import pandas as pd
import matplotlib.py as plt
df=pd.read_csv('star_with_gravity.csv')
df.head()
bools=[]
for d in df.Distance:
  if d<100:
    bools.append(True)
  else:
    bools.append(False)
isdist=pd.Series(bools)
isdist.head()
stardist=df[isdist]
stardist.reset_index(inplace=True,drop=True)
stardist.head()
stardist.shape()
gravitybool=[]
for G in stardist.Gravity:
  if G<=350 and G>=150:
    gravitybool.append(True)
  else:
    gravitybool.append(False)
isgravity=pd.Series(gravitybool)
finalstars=stardist[isgravity]
finalstars.head()
finalstars.shape()
finalstars.reset_index(inplace=True,drop=True)
finalstars.to_csv("filtered_stars.csv")