#1
import os
import pandas as pd

# Create folder
folder_name = "data_experiment"
os.makedirs(folder_name, exist_ok=True)

# Create sample_data.csv
csv_data = """Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago"""
with open(os.path.join(folder_name, "sample_data.csv"), "w") as f:
    f.write(csv_data)

# Create sample_data.json
json_data = [
    {"Name": "David", "Age": 28, "City": "San Francisco"},
    {"Name": "Eve", "Age": 22, "City": "Seattle"}
]
pd.DataFrame(json_data).to_json(os.path.join(folder_name, "sample_data.json"), orient='records')

# Create sample_data.xlsx
excel_data = {
    "Name": ["Frank", "Grace", "Hannah"],
    "Age": [40, 32, 27],
    "City": ["Austin", "Denver", "Boston"]
}
df_excel = pd.DataFrame(excel_data)
df_excel.to_excel(os.path.join(folder_name, "sample_data.xlsx"), index=False)

#2
import pandas as pd
import os

folder_name = "data_experiment"

# Load CSV
csv_file_path = os.path.join(folder_name, "sample_data.csv")
df_csv = pd.read_csv(csv_file_path)
print("CSV Data:")
print(df_csv)

# Filter CSV data
filtered_data = df_csv[df_csv['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)

# Load JSON
json_file_path = os.path.join(folder_name, "sample_data.json")
df_json = pd.read_json(json_file_path)
print("\nJSON Data:")
print(df_json)

# Average age from JSON
average_age = df_json['Age'].mean()
print("\nAverage Age:", average_age)

# Load Excel
excel_file_path = os.path.join(folder_name, "sample_data.xlsx")
df_excel = pd.read_excel(excel_file_path)
print("\nExcel Data:")
print(df_excel)

# Count entries in Excel
entry_count = df_excel.shape[0]
print("\nNumber of entries in Excel file:", entry_count)


#3
# Save filtered CSV
filtered_csv_path = os.path.join(folder_name, "filtered_data.csv")
filtered_data.to_csv(filtered_csv_path, index=False)
print("\nFiltered data saved to 'filtered_data.csv'.")

# Save JSON to new file
new_json_path = os.path.join(folder_name, "new_data.json")
df_json.to_json(new_json_path, orient='records', lines=True)
print("JSON data saved to 'new_data.json'.")

# Save Excel to new file
new_excel_path = os.path.join(folder_name, "new_data.xlsx")
df_excel.to_excel(new_excel_path, index=False)
print("Excel data saved to 'new_data.xlsx'.")