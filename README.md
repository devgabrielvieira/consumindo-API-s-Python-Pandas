# Documentação do Código para Leitura e Filtragem de Dados usando Pandas

A seguir, está a documentação para o código Python que lê dados de uma URL usando a biblioteca `pandas`, converte a coluna de datas para o tipo `datetime` e filtra as linhas com datas a partir de 01/01/2023.

## Introdução

O código fornecido demonstra como usar a biblioteca `pandas` para ler dados de uma URL, realizar a conversão da coluna de datas para o tipo `datetime` e filtrar as linhas com datas a partir de 01/01/2023. O resultado é exibido usando a função `display()` do módulo `IPython.display`.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos antes de executar o código:

- Python (versão 3.x recomendada) instalado no seu sistema.
- As bibliotecas `pandas` e `IPython` instaladas. Caso não estejam instaladas, você pode instalá-las usando os comandos `pip install pandas` e `pip install ipython`.

## Código

Aqui está o código completo para ler e filtrar dados usando o `pandas`:

```python
import pandas as pd
from IPython.display import display as dp

# URL dos dados
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

# Ler os dados da URL
df = pd.read_json(url)

# Converter a coluna 'data' para o tipo datetime
df['data'] = pd.to_datetime(df['data'], dayfirst=True)

# Filtrar as linhas com datas a partir de 01/01/2023
df = df.loc[df['data'] >= '2023-01-01']

# Exibir as primeiras linhas do DataFrame
dp(df.head())
```

## Explicação do Código

1. O código começa importando as bibliotecas `pandas` e `IPython.display`. A segunda importação é necessária para exibir os resultados usando a função `display()`.

2. Uma variável `url` é definida com a URL dos dados a serem lidos.

3. A função `read_json()` do `pandas` é usada para ler os dados da URL especificada e armazená-los em um DataFrame chamado `df`.

4. A coluna 'data' do DataFrame é convertida para o tipo `datetime` usando a função `to_datetime()` do `pandas`. O parâmetro `dayfirst=True` é utilizado para especificar que o formato da data é "dia/mês/ano".

5. O DataFrame é filtrado usando a função `loc[]` do `pandas`. A condição `df['data'] >= '2023-01-01'` é usada para selecionar as linhas com datas a partir de 01/01/2023.

6. O resultado filtrado é exibido usando a função `display()` renomeada como `dp` no import.

## Execução

Para executar o código, siga estas etapas:

1. Certifique-se de ter cumprido todos os requisitos mencionados anteriormente.

2. Crie um novo arquivo Python e copie o código fornecido para o arquivo.

3. Salve o arquivo com um nome adequado, como "api-s.py".

4. Abra um terminal ou prompt de comando e navegue até o

 diretório onde o arquivo Python foi salvo.

5. Execute o arquivo Python digitando o seguinte comando:

   ```
   python api-s.py
   ```

6. Após a execução do código, as primeiras linhas do DataFrame filtrado serão exibidas.

## Conclusão

A documentação acima fornece informações sobre como utilizar o código Python para ler e filtrar dados usando a biblioteca `pandas`. Certifique-se de seguir os requisitos e as etapas de execução mencionadas para obter os resultados desejados.
