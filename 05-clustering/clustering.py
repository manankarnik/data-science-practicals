import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
diabetes = pd.read_csv("diabetes.csv")

# Explore the dataset
print(diabetes.describe())
print(diabetes.columns)

# Prepare data for clustering
new_data = diabetes.drop(columns=['Outcome'])
print(new_data.head())

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(new_data)
diabetes['kmeans_cluster'] = kmeans.labels_

# Elbow method to find optimal k
wss = []
for k in range(1, 16):
 kmeans = KMeans(n_clusters=k, random_state=42)
 kmeans.fit(new_data)
 wss.append(kmeans.inertia_)
plt.plot(range(1, 16), wss, marker='o')
plt.xlabel('Number of clusters k')
plt.ylabel('Total within-clusters sum of square')
plt.show()

# Standardize the data
scaler = StandardScaler()
X_std = scaler.fit_transform(new_data)

# Reduce dimensions for visualization (you can skip this step if you have fewer features)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)

# Visualize the clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans.labels_, cmap='viridis')
plt.title('K-means Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# Silhouette Score for K-Means
silhouette_avg = silhouette_score(new_data, diabetes['kmeans_cluster'])
print("Mean Silhouette Width for K-Means Clustering:", silhouette_avg)

# Hierarchical clustering
linkage_matrix = linkage(new_data, method='ward')
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.show()

# Agglomerative clustering
agglomerative = AgglomerativeClustering(n_clusters=3)
diabetes['hierarchical_cluster'] = agglomerative.fit_predict(new_data)

# Plot Hierarchical clusters
plt.scatter(new_data['Pregnancies'], new_data['Glucose'], c=diabetes['hierarchical_cluster'], cmap='viridis', alpha=0.6, s=50)
plt.xlabel('Pregnancies')
plt.ylabel('Glucose')
plt.title('Hierarchical Clustering')
plt.show()

# Silhouette Score for Hierarchical Clustering
silhouette_avg_hierarchical = silhouette_score(new_data, diabetes['hierarchical_cluster'])
print("Mean Silhouette Width for Hierarchical Clustering:", silhouette_avg_hierarchical)
