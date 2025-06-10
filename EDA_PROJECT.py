import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math_Score': [85, 78, 92, 70, 88],
    'Science_Score': [90, 76, 89, 68, 95],
    'English_Score': [78, 85, 80, 72, 88]
}

df = pd.DataFrame(data)

# 2. Display the first few rows
print("DataFrame:")
print(df.head())

# 3. Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Visualize data
plt.figure(figsize=(6, 4))
sns.heatmap(df.drop('Name', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 6. Bar plot of average scores
df.set_index('Name')[['Math_Score', 'Science_Score', 'English_Score']].plot(kind='bar')
plt.title("Scores by Student")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.show()
