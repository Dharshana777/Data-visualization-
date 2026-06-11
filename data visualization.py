import pandas as pd
import matplotlib.pyplot as plt

# Student Performance Dataset
data = {
    "Student": ["Arun", "Priya", "Kumar", "Divya", "Rahul",
                "Sneha", "Vijay", "Meena", "Ajay", "Pooja",
                "Karthik", "Anu", "Ravi", "Keerthi", "Sanjay"],
    "Marks": [85, 92, 78, 88, 67, 95, 72, 90, 80, 86, 91, 84, 76, 89, 93],
    "Age": [22, 21, 23, 22, 24, 21, 25, 22, 23, 24, 22, 21, 24, 23, 22],
    "Study_Hours": [5, 7, 4, 6, 3, 8, 4, 7, 5, 6, 7, 5, 4, 6, 8]
}

df = pd.DataFrame(data)

print("Dataset Summary")
print(df.describe())

# 1. Bar Chart - Student Marks
plt.figure(figsize=(10,5))
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()

# 2. Line Chart - Marks Trend
plt.figure(figsize=(10,5))
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()

# 3. Pie Chart - Performance Categories
categories = {
    "Excellent": len(df[df["Marks"] >= 90]),
    "Good": len(df[(df["Marks"] >= 75) & (df["Marks"] < 90)]),
    "Average": len(df[df["Marks"] < 75])
}

plt.figure(figsize=(6,6))
plt.pie(categories.values(),
        labels=categories.keys(),
        autopct='%1.1f%%')
plt.title("Performance Distribution")
plt.show()

# 4. Histogram - Marks Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=6)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Study Hours vs Marks
plt.figure(figsize=(8,5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# 6. Box Plot - Outlier Detection
plt.figure(figsize=(6,5))
plt.boxplot(df["Marks"])
plt.title("Marks Box Plot")
plt.ylabel("Marks")
plt.show()

print("\nData Visualization Completed Successfully!")
