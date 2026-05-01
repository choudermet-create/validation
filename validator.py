import pandas as pd
import os

# -----------------------------
# Step 1: File name
# -----------------------------
file_name = "data.xlsx"

# -----------------------------
# Step 2: Create sample Excel (if not exists)
# -----------------------------
if not os.path.exists(file_name):
    data = {
        "Name": ["Ali", "Sara", "John"],
        "Age": [25, 17, None],
        "Email": ["ali@mail.com", "sara@mail.com", "johnmail.com"]
    }

    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)

    print(f"{file_name} created.\n")

# -----------------------------
# Step 3: Load Excel
# -----------------------------
df = pd.read_excel(file_name)

# -----------------------------
# Step 4: Clean Excel data
# -----------------------------

# Clean column names:
# Example: " Name " becomes "Name"
df.columns = df.columns.str.strip()

# Remove rows where everything is empty
df = df.dropna(how="all")

# Reset row index after removing empty rows
df = df.reset_index(drop=True)

# Print what pandas is actually reading
print("Columns found:", df.columns.tolist())
print("\nData found:")
print(df)

# -----------------------------
# Step 5: Validators
# -----------------------------
def is_not_empty(value):
    return pd.notna(value) and str(value).strip() != ""

def is_adult(age):
    return pd.notna(age) and age >= 18

def is_email(value):
    return pd.notna(value) and "@" in str(value)

# -----------------------------
# Step 6: Check required columns exist
# -----------------------------
required_columns = ["Name", "Age", "Email"]

for column in required_columns:
    if column not in df.columns:
        print(f"\nERROR: Missing required column: {column}")
        print("Please check your Excel header names.")
        exit()

# -----------------------------
# Step 7: Validate rows
# -----------------------------
print("\nValidation Results:\n")

for index, row in df.iterrows():
    errors = []

    if not is_not_empty(row["Name"]):
        errors.append("Name is empty")

    if not is_not_empty(row["Age"]) or not is_adult(row["Age"]):
        errors.append("Invalid age")

    if not is_email(row["Email"]):
        errors.append("Invalid email")

    if errors:
        print(f"Row {index + 1} errors: {errors}")
    else:
        print(f"Row {index + 1} is valid")