import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Classifier': ['MLP Classifier', 'SVC classifier', 'RandomForest', 'LogisticRegression', 'Multinomial Naive Bayes'],
    'Accuracy': [0.78, 0.69, 0.71, 0.73, 0.76],
    'F1 Score': [0.78, 0.71, 0.67, 0.71, 0.74]
}

df = pd.DataFrame(data)

import numpy as np

plt.figure(figsize=(12, 6))

# Define the positions for the bars
bar_width = 0.35
index = np.arange(len(df['Classifier']))

# Plot Accuracy scores
plt.bar(index, df['Accuracy'], bar_width, color='skyblue', label='Accuracy')

# Plot F1 scores
plt.bar(index + bar_width, df['F1 Score'], bar_width, color='orange', label='F1 Score')

plt.title('Comparison of F1 Scores and Accuracy Scores for Classifiers')
plt.xlabel('Classifier')
plt.ylabel('Score')
plt.legend()
plt.xticks(index + bar_width / 2, df['Classifier'], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
