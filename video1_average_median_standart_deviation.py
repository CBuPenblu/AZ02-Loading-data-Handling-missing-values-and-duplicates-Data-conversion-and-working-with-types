import pandas as pd

data = {
    'Age': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Salary': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000]
}

df = pd.DataFrame(data)

#print(df.describe())

print(f"Average age - {df['Age'].mean()}")
print(f"Median age - {df['Age'].median()} ")
print(f"Standart age deviation - {df['Age'].std()} ")

print(f"Average salary - {df['Salary'].mean()} ")
print(f"Median salary - {df['Salary'].median()} ")
print(f"Standart salary deviation - {df['Salary'].std()} ")