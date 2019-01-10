from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd
import numpy as np
from bokeh.core.properties import value

all_data = pd.read_csv("relevantQs.csv", delimiter=',')

d_age_s = dict()
for index, row in all_data.iterrows():
    if np.isnan(row['Q48']) or row['Q48'] == 999.0:
            continue
    age = int(row['Q48'])
    if row['Q48'] not in d_age_s:
        d_age_s[age] = {'Male': 0, 'Female': 0}
        if row['Q47'] == 'Man':
            d_age_s[age]['Male'] = 1
        elif row['Q47'] == 'Vrouw':
            d_age_s[age]['Female'] = 1
        else: 
            continue
    else:
        if row['Q47'] == 'Man':
            d_age_s[age]['Male'] += 1
        elif row['Q47'] == 'Vrouw':
            d_age_s[age]['Female'] += 1

d_age_s = {str(key):d_age_s[key] for key in d_age_s}
sorted_age_gender = sorted(d_age_s)

output_file("participants_age_gender.html")

ages = [age for age in sorted_age_gender]
genders = ["Male", "Female"]
colors = ["#718dbf", "#e84d60"]

data = {'ages' : ages,
        'Male'   : [d_age_s[age]['Male'] for age in sorted_age_gender],
        'Female' : [d_age_s[age]['Female'] for age in sorted_age_gender]}

p = figure(x_range=ages, plot_height=500, plot_width=1000, title="Participants age per gender",
           toolbar_location=None, tools="")

p.vbar_stack(genders, x='ages', width=0.9, color=colors, source=data, legend=[value(x) for x in genders])

p.y_range.start = 0
p.y_range.end = 80
p.x_range.range_padding = 0.01
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)