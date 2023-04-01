import pandas as pd

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
df = pd.read_json(url)
print(df.head())