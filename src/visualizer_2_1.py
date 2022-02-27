import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import myConvexHull

data = datasets.load_wine()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.head())

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
idxA = 0
idxB = 1
plt.title((data.feature_names[idxA] + " vs " + data.feature_names[idxB]))
plt.xlabel(data.feature_names[idxA])
plt.ylabel(data.feature_names[idxB])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[idxA,idxB]].values
    hull = myConvexHull.myConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
        
plt.legend()
plt.show()
