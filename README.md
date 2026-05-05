# Customer-Segmentation
This project groups customers based on their behavior and demographics using KMeans Clustering. It helps businesses understand customer types and improve marketing strategies through data analysis and visualization.

# Customer Segmentation Project

## Overview
This project focuses on segmenting customers based on their behavior and demographic details. The goal is to group similar customers together so businesses can better understand their needs and improve decision-making.

## Objective
- Analyze customer data such as age, income, and spending habits  
- Group customers into different segments  
- Visualize customer clusters using graphs  

## Method Used
We used the machine learning algorithm **KMeans Clustering** to divide customers into 3 groups based on similarity.

## 📊 Dataset Details
The dataset contains 100 customer records with the following attributes:
- CustomerID  
- Age  
- Gender  
- Income  
- SpendingScore  
- PurchaseFrequency  
- Region  

## Technologies Used
- Python  
- Pandas  
- Matplotlib  
- Scikit-learn  

## How It Works
1. Load the dataset from CSV file  
2. Convert categorical data (Gender, Region) into numeric format  
3. Select important features for clustering  
4. Apply KMeans clustering algorithm  
5. Visualize the results using a scatter plot  

## Output
- Customers are grouped into 3 clusters  
- Each cluster represents a type of customer (high, medium, low value)  
- A graph is generated showing Income vs Spending Score  

## Applications
- Targeted marketing  
- Customer behavior analysis  
- Business decision making  

## How to Run
pip install pandas matplotlib scikit-learn
python customerSegmentation.py
