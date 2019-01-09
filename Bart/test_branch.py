import numpy as np
import pandas as pd

# return pandas dataframe given csv file
def load_data(filename):
	return pd.read_csv(filename, delimiter=';')


if __name__ == "__main__":
	alldata = load_data("VragenlijstdeelnemersDamtotDamloop_bewerkt_anoniem.csv")
	print(alldata.head())
