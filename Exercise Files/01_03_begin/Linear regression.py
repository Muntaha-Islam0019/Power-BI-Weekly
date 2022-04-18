import pandas as pd
import numpy as np

dataset = pd.read_csv(r'C:/Users/LinkedIn Instructor/Desktop/Exercise Files/Data Sources/New York City weather.csv')
dataset = dataset[dataset['date']>='2010-01-01'].dropna()
print(dataset)

m = np.polyfit(dataset['TMIN'],dataset['TMAX'],1)
f = np.poly1d(m)
print(f)
dataset.insert(2,'Best Fit Line', f(dataset['TMIN']))
print(dataset)