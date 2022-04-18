import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv(r'C:/Users/LinkedIn Instructor/Desktop/Exercise Files/Data Sources/ERCOT electricity.csv').dropna().drop(columns=['Demand']).melt(id_vars=['Date'], var_name='Energy Source', value_name='Megawatt Hours')
dataset = dataset.groupby('Energy Source').agg({'Megawatt Hours': [np.mean, np.median]})
print(dataset)

#dataset = dataset.set_index('Energy Source')
sns.clustermap(dataset.T, cmap = 'RdYlBu')
plt.rcParams.update({'font.size': 22})
plt.show()