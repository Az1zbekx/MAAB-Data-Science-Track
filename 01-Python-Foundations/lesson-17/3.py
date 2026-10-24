import pandas as pd

# 1. Load Titanic data
titanic = pd.read_csv('titanic.csv')

# 2. Group by Pclass and calculate required stats
grouped = titanic.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'  # Count of passengers
}).rename(columns={'PassengerId': 'PassengerCount'}).reset_index()

print(grouped)
