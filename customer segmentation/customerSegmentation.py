import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("data/customerData.csv")
g=LabelEncoder()
r=LabelEncoder()
data['Gender']=g.fit_transform(data['Gender'])
data['Region']=r.fit_transform(data['Region'])
X=data[['Age','Income','SpendingScore','PurchaseFrequency','Gender','Region']]
k=KMeans(n_clusters=3,random_state=42)
data['Cluster']=k.fit_predict(X)
print(data.head())
plt.scatter(data['Income'],data['SpendingScore'],c=data['Cluster'])
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation')
plt.show()