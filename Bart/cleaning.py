import numpy as np
import pandas as pd
import regex as re

# return pandas dataframe of csv file
def load_data(filename, delim):
	return pd.read_csv(filename, delimiter=delim)

# Filters all subjects who didnt train
def filter_unusable(data):
	data = data.loc[data["Q1"] == "Ja"]
	data = data.loc[data["Q4"] != "Nee"]
	cols_to_drop = list(data.columns[:9]) + list(data.columns[40:159]) + list(data.columns[-2:]) + [x for x in data.columns if re.match(r'Q\d\d[A-Z]{0,1}[_]', x)]
	return data.drop(cols_to_drop, axis=1)

# filters all subject who didnt fill in the Qs
def filter_more(data):
	data = data.reset_index(drop=True)
	data = data.replace(" ", np.nan)
	nan = [index for index, row in data.iterrows() if row.isnull().sum() == 62]
	data = data.drop(data.index[nan])
	return data

# converts numeric data to floats
def str_to_int(data):
	Qs = ['Q48', 'Q49', 'Q50']
	data['Q49'] = data['Q49'].apply(lambda x: x.replace(',','.'))
	data["Q50"] = data['Q50'].apply(lambda x: x.replace(',','.'))
	for Q in Qs:
		data[Q] = pd.to_numeric(data[Q])
		mask = data[Q] > 220
		data.loc[mask, Q] = 0
	return data

# makes a csv file with all relevant Qs/subjects
if __name__ == "__main__":
	all_data = load_data("data.csv", ";")
	data = filter_unusable(all_data)
	data = filter_more(data)
	data = str_to_int(data)
	data.to_csv("clean_data.csv")
