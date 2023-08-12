#%%
import pandas as pd

#%%

df = pd.read_csv("../example_data/pedido.csv")
# %%

df
# %%
df[['idPedido','descUF']].sample(500).head(10)
# %%
 
filtro_colunas =[
    'idPedido',
    'descUF',
    'txtRecado'
]

df = df[filtro_colunas]
df
# %%
df_sample = df.sample(550)
# %%
df_sample.iloc[34]

#%%
df_sample.iloc[23:98]

#%%

df_sample.iloc[10:12][['idPedido','dtPedido']]