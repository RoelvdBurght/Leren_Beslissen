import matplotlib.pyplot as plt
import pandas as pd

path = "/home/roel/PycharmProjects/Leren_Beslissen/data.csv"
df = pd.read_csv(path)

for col in df.columns:
    print(col)

