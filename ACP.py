
# Import required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a dataset using Pandas
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha',
             'Arjun', 'Kiran', 'Riya'],
    'Maths': [85, 90, 78, 92, 88, 76, 95, 89],
    'Science': [80, 95, 82, 90, 85, 79, 92, 88],
    'English': [75, 88, 80, 95, 82, 85, 90, 91]
}

df = pd.DataFrame(data)

# 2. Display the dataset
print("Student Dataset:")
print(df)

# 3. Display first five rows
print("\nFirst five rows:")
print(df.head())

# 4. Dataset information
print("\nDataset Information:")
df.info()

# 5. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 6. NumPy operations
maths_marks = np.array(df['Maths'])

print("\nNumPy Operations")
print("Maths Marks:", maths_marks)
print("Total Marks:", np.sum(maths_marks))
print("Average Marks:", np.mean(maths_marks))
print("Maximum Marks:", np.max(maths_marks))
print("Minimum Marks:", np.min(maths_marks))
print("Standard Deviation:", np.std(maths_marks))

# 7. Add a Total and Average column
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Maths', 'Science', 'English']].mean(axis=1)

print("\nDataset with Total and Average:")
print(df)

# 8. Find the student with the highest total
top_student = df.loc[df['Total'].idxmax()]
print("\nTop Performing Student:")
print(top_student)

# 9. Sort students by total marks
print("\nStudents Sorted by Total Marks:")
print(df.sort_values(by='Total', ascending=False))

# 10. Bar chart of total marks
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='Name', y='Total', color='skyblue')
plt.title('Total Marks of Students')
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.tight_layout()
plt.show()

# 11. Line graph of subject marks
plt.figure(figsize=(10, 5))
plt.plot(df['Name'], df['Maths'], marker='o', label='Maths')
plt.plot(df['Name'], df['Science'], marker='s', label='Science')
plt.plot(df['Name'], df['English'], marker='^', label='English')
plt.title('Subject-wise Marks Comparison')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 12. Correlation heatmap
plt.figure(figsize=(7, 5))
correlation = df[['Maths', 'Science', 'English']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm',
            vmin=-1, vmax=1)
plt.title('Correlation Between Subjects')
plt.tight_layout()
plt.show()

# 13. Distribution of Maths marks
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Maths', bins=5, kde=True)
plt.title('Distribution of Maths Marks')
plt.xlabel('Maths Marks')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.show()
