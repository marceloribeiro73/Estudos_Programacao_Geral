#%%
import pandas as pd

#%%

df = pd.read_csv('../example_data/item_pedido.csv')

#%%

df = df.rename(columns={'descTipoItem':'desc_tipo_item'})
#%%
df

#%%
df.rename(columns={'desc_tipo_item': 'descTipoItem'}, inplace=True)

df