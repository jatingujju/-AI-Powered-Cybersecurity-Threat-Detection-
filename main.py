import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/KDDTrain+.txt", header=None)

print(df.head())
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)