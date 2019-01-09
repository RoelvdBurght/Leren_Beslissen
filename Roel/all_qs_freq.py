import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data_old.csv", delimiter=";")

bins = []
bin_freqs = []
column_names = []
for col in df.columns:
    column_names.append(col)
print(df.shape)

base, _ = df.shape
freq = []
for col in column_names:
    c = 0
    for entry in df[col]:
        if entry == " " or pd.isna(entry):
            c += 1
    freq.append(base - c)

bars = []
for i in range(len(freq)):
    bars.append(i)

plt.bar(bars, freq)
plt.xlabel("Vraag nummer")
plt.ylabel("Aantal ingevulde entrys")
plt.title("Frequentie antwoorden per vraag")
plt.show()
