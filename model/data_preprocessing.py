import pandas as pd

df = pd.read_csv("../data/Bank Customer Churn Prediction.csv")

df = df.drop(columns=["customer_id"])

df = pd.get_dummies(df, columns=["country", "gender"], drop_first=True)

print(df.isnull().sum())

df.to_csv("../data/cleaned_data.csv", index=False)
print("Cleaned data saved")
