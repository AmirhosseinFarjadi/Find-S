import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\AmirHossin\Desktop\CandidateElminate\DataSet1.csv")
attribute=np.array(df)[:,:-1]
target=np.array(df)[:,-1]
attribute_len=len(attribute[0])
specific_hypothesis=[0]*attribute_len
print(target[0])
for i in range(len(target)):
    if target[i]=="yes":
        specific_hypothesis=attribute[i,:]
        index_yes=i
        break
    else:
        continue
 
for z in range(index_yes+1,len(attribute)):
    if target[z]=="yes":
        vector_sample=attribute[z,:]
        for k in range(len(attribute[0])):
            if vector_sample[k]!=specific_hypothesis[k]:
                specific_hypothesis[k]="?"
            else:
                continue
    else:
        continue

print(specific_hypothesis)