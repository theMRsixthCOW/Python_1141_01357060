from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].map({
    0: 'setosa',    
      1: 'versicolor',
        2: 'virginica'    
    })

X = df[iris.feature_names].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

#cluster
print("Species in each cluster:")
for cluster_id in range(3):
    cluster_data = df[df['cluster'] == cluster_id]
    dominant_species = cluster_data['species'].mode()[0]  #
    count = cluster_data['species'].value_counts().max()
    total = len(cluster_data)
    print(f"Cluster {cluster_id}: {dominant_species} ({count}/{total} samples)")

print("\nCluster mapping:")
cluster_all = df.groupby('cluster')['species'].apply(lambda x: x.mode()[0])
print(cluster_all)