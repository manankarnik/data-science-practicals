import pandas as pd
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

##### Performance #####
# Silhouette score for clustering: 0.416
# Indicates relatively good clustering performance
# Implies well-separated and dense clusters
# Clustering algorithm effectively groups similar data points together

# Accuracy score for classification: 0.525
# Slightly above random guessing
# Indicates poor performance of the classification model
# Predictions are not significantly better than chance

# Clustering algorithm captures underlying patterns in the data
# Classification model requires further refinement or additional features
# Further investigation and experimentation needed to understand factors influencing model performance
# Enhancing accuracy of the classification model is necessary


# Load the dataset
data = pd.read_csv("customers.csv")

# Clustering
X_cluster = data[['Age', 'Annual_Income', 'Spending_Score']]
kmeans = KMeans(n_clusters=6, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_cluster)

# Plot clustering results
sns.scatterplot(x='Annual_Income', y='Spending_Score', hue='Cluster', data=data, palette='viridis', legend='full')
plt.title('Clustering Results')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

# Classification
X_classification = data[['Age', 'Annual_Income', 'Spending_Score']]
y_classification = data['Gender']
X_train, X_test, y_train, y_test = train_test_split(X_classification, y_classification, test_size=0.2, random_state=42)
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Performance Evaluation
cluster_silhouette_score = silhouette_score(X_cluster, data['Cluster'])
classification_accuracy = accuracy_score(y_test, y_pred)

print("Silhouette Score for Clustering:", cluster_silhouette_score)
print("Accuracy Score for Classification:", classification_accuracy)

# Plot decision tree
plot_tree(classifier, filled=True, feature_names=X_classification.columns, class_names=['Female', 'Male'])
plt.title('Decision Tree')
plt.show()
