import matplotlib.pyplot as plt
import numpy as np
import regex as re
import cleaning

def drop_col_same_Q(data):
    drop_cols = [x for x in data.columns if re.match(r'Q\d\d[^A]', x)]
    return data.drop(drop_cols, axis=1)

def plot_Qs_rate(data):
    N = len(data)
    not_answered_N = N - data.count()
    plt.bar(data.columns[1:], not_answered_N[1:]/N*100)
    plt.xticks(rotation=45)
    plt.show()

def some_more_info(data):
    not_answered_N = len(data) - data.count()
    print(not_answered_N)
    # people that didnt have to answer q12
    q11 = sum(data['Q11'] == 'Ik wil niet vaker en/of meer kilometers hardlopen dan ik nu doe')
    q12 = sum(data['Q12A'].isnull())
    # people that skipped q12 unleggit
    print(q12-q11)

if __name__ == "__main__":
    data = cleaning.load_data("relevantQS.csv", ",")
    data = data.replace(" ", np.nan)
    data = drop_col_same_Q(data)
    some_more_info(data)
    plot_Qs_rate(data)
