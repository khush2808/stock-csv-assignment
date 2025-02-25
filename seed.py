import pandas as pd

# Load the CSV file
input_file = "dump.csv"  # Replace with your actual file path
output_file = "seed.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Convert index_date to datetime format for sorting
df["index_date"] = pd.to_datetime(df["index_date"], format="%Y-%m-%d")

# Group by index_name (Company Name) and sort by date in ascending order
df_sorted = df.sort_values(by=["index_name", "index_date"])

# Export to a new CSV file
df_sorted.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")
