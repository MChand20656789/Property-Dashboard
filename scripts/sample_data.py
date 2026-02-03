import pandas as pd

src = "data/realtor-data.csv"
out = "data/real_estate_sample.csv"
n = 3000  # sample size

df = pd.read_csv(src, low_memory=False)
# quick cleaning: drop rows missing these core fields
df = df.dropna(subset=["price", "city", "state", "house_size"])
# sample
df_sample = df.sample(n=n, random_state=42)
df_sample.to_csv(out, index=False)
print(f"Saved sample {out} with {len(df_sample)} rows")