
import pandas as pd
from faker import Faker
import random

#Initailize Faker
fake = Faker()

#set a random seed for reproducibility
random.seed(42)
fake.seed_instance(42) #to make sure Faker generates the same random values each time as it also had its own randomness stored somewhere in the module 

#Generate and print a fake name
#We only need a placeholder like _ to run the loop and didn't necessarily need it for generating sequential user IDs.
users = []
for i in range(1, 21):
    user = {
        "user_id": "PWR" + str(100 + i),
        "name": fake.name(),
        "age": random.randint(18,60),
        "country": fake.country(),
        "group": random.choice(["A", "B"]),
        "clicks": random.randint(0,20),
        "converted": random.choice([0, 1])
    }
    users.append(user)

#Create DataFrame
df = pd.DataFrame(users)

#to shift the default index from 0 to 1 in pandas
df.index = df.index + 1

print(df)

#below is done to save the data in a csv file 
#df.to_csv("ab_testing_data.csv", index=False)

print("="*50)
print("Wohoo! Data saved successfully, 1/3rd of your project is complete!")

## ==================== For Pandas Functions ==================================#

# ==================== Dataset Overview ====================
print("\n" + "="*50)
print("Dataset Overview")
print("="*50)

print("\nLoading the dataset...")
df = pd.read_csv("ab_testing_data.csv") #loading the dataset

# ==================== Summary of Dataset ====================
print("\n" + "="*50)
print("Summary of dataset (Column types and missing values)")
print("="*50)
print(df.info()) #summary of dataset(column types, missing values to help understand the structure of data)
print("="*50)

# ==================== Summary Statistics ====================
print("\n" + "="*50)
print("Summary Stats (Numerical Data)")
print(df.describe()) #shows statistics for numerical columns useful for understanding age distribution, clicks and conversion rates
print("="*50)

# ==================== A/B Test Group Distribution ====================
print("\n" + "="*50)
print("User Distribution in A/B test groups")
print(df["group"].value_counts()) #counts users in Group A & B to ensure balanced users in A/B testing groups
print("="*50)

# ==================== A/B Test Analysis ====================
#calculated average clicks and conversion rate for each group to help compare Group A and Group B on engagement and conversions
print("\n" + "="*50)
print("A/B test analysis results (Average clicks and conversion rates)")
group_analysis = df.groupby("group").agg({
    "clicks": "mean",
    "converted": "mean"
})
print(group_analysis)
print("="*50)

# ==================== Saving Cleaned Dataset ====================
df.to_csv("cleaned_ab_testing_data_pandas.csv", index=False) #save cleaned daatset for NumPy analysis or deeper Pandas analysis

print("\n" + "="*50)
print("Wohoo! You just learnt how to use basic panda functions and completed 2/3rd of your overall project!")
print("="*50)