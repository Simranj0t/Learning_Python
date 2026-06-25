import pandas as pd
import numpy as np

dict1 = {
    "name" : ["Ram","Sham","Sita","Gita"],
    "Class" : ["9","7","6","10"]
}

df = pd.DataFrame(dict1)
print(df)

df.to_csv("Sample.csv")
df.to_csv("Sample.csv",index=False)

simran = pd.read_csv("TrainDetails.csv")
simran
simran["pf no"][0] = 6
