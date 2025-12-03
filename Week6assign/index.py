
import numpy as np
import pandas as pd

# ------------------------------
# Loading your dataset
# ------------------------------
df = pd.read_csv("Myers Briggs Table_S1.csv")

# ------------------------------
# Preparing the sample data (first 5 rows)
# Creating unique names as MBTI_SNO
# ------------------------------
sample = df.head(5).copy()
sample["name"] = sample["MBTI"] + "_" + sample["S No"].astype(str)

# Extracting required fields
names = sample["name"].values
ages = sample["AGE"].values
heights = sample["HEIGHT"].values

# ------------------------------
# TASK A: Create structured array
# ------------------------------

data_type = [
    ("name", "U20"),     # string
    ("age", "i4"),       # integer
    ("height", "f4")     # float
]

structured_array = np.zeros(5, dtype=data_type)

structured_array["name"] = names
structured_array["age"] = ages
structured_array["height"] = heights

print("TASK A: Structured Array")
print(structured_array)
print("\n")

# ------------------------------
# TASK B: Print all values of the 'name' field
# ------------------------------
print("TASK B: All Names")
print(structured_array["name"])
print("\n")

# ------------------------------
# TASK C: Update the age of the first individual to 30
# ------------------------------
structured_array["age"][0] = 30

print("TASK C: After Updating First Person's Age to 30")
print(structured_array)
print("\n")

# ------------------------------
# TASK D: Add a new record (Nadine Smith, 25, 5.9)
# ------------------------------
new_record = np.array([("Nadine Smith", 25, 5.9)], dtype=data_type)

updated_array = np.concatenate((structured_array, new_record))

print("TASK D: After Adding Nadine Smith")
print(updated_array)
