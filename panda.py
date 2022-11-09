import pandas as pd

# ✅ works
df = pd.DataFrame(
    {
        "Name": [
            "Alice",
            "Bob",
            "Carl",
        ],
        "Age": [29, 30, 31],
    }
)

print(df)