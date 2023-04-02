import pandas as pd
from IPython.display import display as dp

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
df = pd.read_json(url)

# Converter a coluna 'data' para o tipo datetime
df['data'] = pd.to_datetime(df['data'], dayfirst=True)

# Filtrar as linhas com datas a partir de 01/01/2023
df = df.loc[df['data']>= '2023-03-01']

dp(df.head())