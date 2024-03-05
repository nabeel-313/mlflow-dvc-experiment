import pandas as pd

data = [
    {"name": "Nabeel", "age": 28, "city": "Pune"},
    {"name": "Momin", "age": 22, "city": "Mumbai"},
    {"name": "Ahmed", "age": 32, "city": "Hyderbad"},
    {"name": "Riyaz", "age": 55, "city": "Banglore"}
]
Data = pd.DataFrame(data)
Data.to_csv("data/data.csv", index=False)

