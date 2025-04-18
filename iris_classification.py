# iris_classification.py

# Step 1: Import Libraries

import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 2: Load Dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Step 3: Explore Data
print("\n=== First 5 Rows of Data ===")
print(df.head())

print("\n=== Dataset Information ===")
print(df.info())

print("\n=== Class Distribution ===")
print(df['species'].value_counts())

# Step 4: Visualize Data
plt.figure(figsize=(10, 6))
sns.pairplot(df, hue='species', palette='Dark2')
plt.suptitle('Iris Species Feature Relationships', y=1.02)
plt.savefig('iris_pairplot.png')  # Saves visualization to file
plt.show()

# Step 5: Prepare Data for Training
X = df[['sepal length (cm)', 'sepal width (cm)', 
        'petal length (cm)', 'petal width (cm)']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y
)

# Step 6: Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 7: Evaluate Model
y_pred = model.predict(X_test)

print("\n=== Model Evaluation ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 8: Save Model
joblib.dump(model, 'iris_classifier.joblib')
print("\nModel saved as 'iris_classifier.joblib'")