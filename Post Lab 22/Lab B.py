import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, np.nan],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values in 'Age' column with the mean
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

print("\nDataFrame after filling missing values with mean:")
print(df)