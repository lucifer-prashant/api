import pandas as pd

USD_TO_INR = 83

def convert_to_inr(amount_str):
    if pd.isna(amount_str):
        return None
    amount_str = amount_str.replace('$', '').replace('+', '').strip()
    if 'Bn' in amount_str:
        value = float(amount_str.replace('Bn', '').strip()) * 1_000_000_000
    elif 'Mn' in amount_str:
        value = float(amount_str.replace('Mn', '').strip()) * 1_000_000
    else:
        return None
    return int(value * USD_TO_INR)

df = pd.read_csv("companies.csv")

df["amount_raised_inr"] = df["amount_raised"].apply(convert_to_inr)
df["amount_raised_inr"] = df["amount_raised_inr"].apply(
    lambda x: f"Rs {x:,}" if pd.notna(x) else None
)

df.drop(columns=["amount_raised"], inplace=True)

df.to_csv("comp.csv", index=False)
