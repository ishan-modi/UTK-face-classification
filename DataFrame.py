import os
import pandas as pd
import numpy as np

data=pd.DataFrame(columns=['age','gender','race','location'])

cnt=0
for a,b,c in os.walk('UTK-face-classification/UTKFace'):
    for j in c:
        try:
            l=j.split('_')
            l.pop()
            l.append('UTKFace/'+j)
            s=pd.Series(l,index=data.columns)
            data=data.append(s,ignore_index=True)
        except:
            continue

data.to_csv('UTK-face-classification/data.csv')