import pandas as pd

data = {
    'Имя': ['Ученик1', 'Ученик2', 'Ученик3', 'Ученик4', 'Ученик5', 'Ученик6', 'Ученик7', 'Ученик8', 'Ученик9', 'Ученик10'],
    'Математика': [90, 75, 88, 92, 85, 78, 95, 80, 84, 77],
    'Физика': [85, 80, 79, 88, 90, 75, 93, 77, 83, 78],
    'Химия': [78, 85, 88, 90, 84, 79, 86, 81, 80, 75],
    'Биология': [80, 82, 85, 87, 88, 81, 83, 84, 79, 76],
    'Литература': [85, 87, 89, 90, 92, 83, 84, 88, 80, 81]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"\nQ1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")
print(f"IQR для оценок по математике: {IQR_math}")

std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
