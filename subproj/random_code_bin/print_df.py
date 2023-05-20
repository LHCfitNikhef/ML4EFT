import pandas as pd
import os 
import sys

path = sys.argv[1]
path_str = str(path)
df = pd.read_pickle(path_str, compression="infer")

print(df)