import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

# ==================== Initialize Faker & Set Seed ====================
fake = Faker()
random.seed(42)
fake.seed_instance(42)  # Ensures reproducibility

# ==================== Generate Fake User Data ====================
users = []
for i in range(1, 21):
    user = {
        "user_id": "PWR" + str(100 + i),
        "name": fake.name(),
        "age": random.randint(18, 60),
        "country": fake.country(),
        "group": random.choice(["A", "B"]),
        "clicks": random.randint(0, 20),
        "converted": random.choice([0, 1])
    }
    users.append(user)

# Create DataFrame
df = pd.DataFrame(users)

# Shift index to start from 1
df.index = df.index + 1

# Save dataset
df.to_csv("ab_testing_data.csv", index=False)

print("="*50)
print("Wohoo! Data saved successfully, 1/3rd of your project is complete!")

# ==================== Load Dataset for Analysis ====================
print("\n" + "="*50)
print("Loading and Analyzing Dataset with Pandas and NumPy")
print("="*50)

df = pd.read_csv("ab_testing_data.csv")  # Load dataset

# ==================== Summary Statistics ====================
print("\n" + "="*50)
print("Summary Stats (Numerical Data)")
print(df.describe())  
print("="*50)

# ==================== NumPy-Based Statistical Analysis ====================
print("\n" + "="*50)
print("NumPy-Based Statistical Analysis")
print("="*50)

clicks = df["clicks"].values  # Convert Pandas column to NumPy array

# NumPy Calculations
print(f"Average Clicks per User: {np.mean(clicks):.2f}")
print(f"Median Clicks per User: {np.median(clicks)}")
print(f"Click Standard Deviation: {np.std(clicks):.2f}")
print(f"Click Variance: {np.var(clicks):.2f}")
print(f"Min Clicks: {np.min(clicks)}, Max Clicks: {np.max(clicks)}")
print(f"25th Percentile Clicks: {np.percentile(clicks, 25)}")
print(f"75th Percentile Clicks: {np.percentile(clicks, 75)}")
print("="*50)

# ==================== A/B Test Analysis ====================
print("\n" + "="*50)
print("A/B Test Analysis (Average Clicks & Conversion Rates)")
print("="*50)

group_analysis = df.groupby("group").agg({
    "clicks": "mean",
    "converted": "mean"
})
print(group_analysis)
print("="*50)

# ==================== Data Visualization ====================

# Set Seaborn style
sns.set_style("whitegrid")

# 1 Histogram of Clicks
def histogram_of_clicks():
    plt.figure(figsize=(8,5))
    sns.histplot(df["clicks"], bins=10, kde=False, color="skyblue", stat="count")
    plt.title("Distribution of Clicks per User")
    plt.xlabel("Number of Clicks")
    plt.ylabel("Frequency")
    plt.yticks(range(0, len(df)+1, 1))
    plt.show()

# 2️ Box Plot for Clicks
def box_plot_for_clicks():
    plt.figure(figsize=(6,5))
    sns.boxplot(x=df["clicks"], color="orange")
    plt.title("Box Plot of Clicks per User")
    plt.xlabel("Number of Clicks")
    plt.show()

# 3️ Bar Chart for A/B Group Clicks
def bar_chart_for_group_clicks():
    plt.figure(figsize=(6,5))
    sns.barplot(x=df["group"], y=df["clicks"], estimator=np.mean, palette="viridis")
    plt.title("Average Clicks by A/B Test Group")
    plt.xlabel("Test Group")
    plt.ylabel("Average Clicks")
    plt.show()

# 4️ Pie Chart for Conversion Rates
def pie_chart_for_conversion_rates():
    conversion_counts = df["converted"].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(conversion_counts, labels=["Not Converted", "Converted"], autopct="%1.1f%%", colors=["red", "green"])
    plt.title("Conversion Rate Distribution")
    plt.show()

# 5️ Scatter Plot (Clicks vs Age)
def scatter_plot():
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df["age"], y=df["clicks"], hue=df["group"], palette="coolwarm")
    plt.title("Clicks vs Age (A/B Groups)")
    plt.xlabel("Age")
    plt.ylabel("Number of Clicks")
    plt.show()

# ==================== Save Cleaned Data ====================
df.to_csv("cleaned_ab_testing_data_numpy.csv", index=False)

print("\n" + "="*50)
print("Wohoo! You just learned how to use NumPy, Pandas & Matplotlib together and completed 3/3rd of your overall project! 🚀")
print("="*50)

# ==================== Menu for user interaction ====================
while(True):
    print("\n1. Histogram of Clicks")
    print("2. Box Plot for Clicks")
    print("3. Bar Chart for A/B Group Clicks")
    print("4. Pie Chart for Conversion Rates")
    print("5.Scatter Plot (Clicks vs Age")
    print("6. Exit the program")

    choice = str(input("Choose an option (1/2/3/4/5/6): "))

    print(f"User entered: {choice}")
    if choice == "1":
        print("Calling Histogram of Clicks")
        histogram_of_clicks()
    elif choice == "2":
        print("Calling Box Plot for Clicks")
        box_plot_for_clicks()
    elif choice == "3":
        print("Calling Bar Chart for Group Clicks")
        bar_chart_for_group_clicks()
    elif choice == "4":
        print("Calling Pie Chart for Conversion Rates")
        pie_chart_for_conversion_rates()  
    elif choice == "5":
        print("Calling Scatter Plot")
        scatter_plot()
        break
    elif choice == "6":
        print("Exiting program. Goodbye!")
    else:
	    print("Invalid choice! Please enter 1,2,3,4,5 or 6.")