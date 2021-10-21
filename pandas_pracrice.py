from matplotlib import colors
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from pandas.core.indexes import category

# read from csv file:
data = pd.read_csv(r'C:\\Users\\azili\\OneDrive\Documents\\Netflix_project\\Cleared_Data.csv', index_col= 'show_id')
df = DataFrame(data)

# add a date culoumn based on existed column 'date_added'.
# extract year, month and weekday from datetime and add these as culomns in data:
# reminder- dt = datetime!
date = pd.to_datetime(data['date_added'])
data['date'] = date
data['year'] = df['date'].dt.year.astype('Int64')
data['month'] = df['date'].dt.month.astype('Int64')
data['weekday'] = df['date'].dt.day_name()

# filter by type:
movies = data[(data['type']=='Movie')]
tv_shows = data[(data['type']=='TV Show')]
# print(movies[['type', 'year']])

# group by:
by_years = data.groupby(['year']).size()
by_months = data.groupby(['month']).size()
by_weekday = data.groupby(['weekday']).size()

# visualization- movies vs. tv-shows:
a = np.array([len(movies), len(tv_shows)])
mylabels = ['movies', 'tv-shows']
mycolors = ['#708090', '#B0C4DE']
plt.pie(a, labels= mylabels, startangle= 90, shadow = True, colors= mycolors, autopct='%1.1f%%')
#plt.show()
