import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "Data", "travel_dataset.csv")

df = pd.read_csv(DATA_PATH)



# Remove unwanted column if present
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# Fill missing values
df["Weekly Off"] = df["Weekly Off"].fillna("No Weekly Off")

df["City"] = df["City"].astype(str).str.strip()
df["City_lower"] = df["City"].str.lower()


# Take source city input
# Take source city input (case-insensitive)
source_city = input("Enter source city: ").strip().lower()

# Create a lowercase City column for comparison
df["City_lower"] = df["City"].str.lower()

# Check city exists

if source_city not in df["City_lower"].values:
    print("Source city not found in dataset")
    print("Available cities are:")
    print(df["City"].unique())
    exit()

# Get source city details
source_row = df[df["City_lower"] == source_city].iloc[0]
source_city = source_row["City"]
source_state = source_row["State"]
source_zone = source_row["Zone"]

# Simple distance score
def distance_score(row):
    if row["City"] == source_city:
        return 1.0
    elif row["State"] == source_state:
        return 0.7
    elif row["Zone"] == source_zone:
        return 0.5
    else:
        return 0.3

df["distance_score"] = df.apply(distance_score, axis=1)

# Filter weekend-friendly places
df = df[(df["time needed to visit in hrs"] <= 5) &
        (df["Google review rating"] >= 4.0)]

# Normalize rating & popularity
df["rating_norm"] = df["Google review rating"] / df["Google review rating"].max()
df["popularity_norm"] = df["Number of google review in lakhs"] / df["Number of google review in lakhs"].max()

# Final score
df["final_score"] = (
    0.4 * df["distance_score"] +
    0.4 * df["rating_norm"] +
    0.2 * df["popularity_norm"]
)

# Show top 5 destinations
result = df.sort_values(by="final_score", ascending=False).head(5)

print("\nTop Weekend Getaways:\n")
print(result[[
    "Name",
    "City",
    "State",
    "Google review rating",
    "Number of google review in lakhs",
    "final_score"
]].to_string(index=False))
