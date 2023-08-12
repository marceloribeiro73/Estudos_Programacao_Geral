#%% 
import pandas as pd

#%%

df = pd.read_csv('../example_data/item_pedido.csv')
df
#%%

filtro_tipo = df['descTipoItem'] == 'bebida'
filtro_tipo
#%%
df[filtro_tipo]

#%%
filtro_tipo_desc = (df['descTipoItem'] == 'bebida') & (df['idPedido'] != 0)
#filtro_tipo_desc
df[filtro_tipo_desc]

#%%
filtro_massas_bebidas = ((df['descTipoItem'] == 'massa') & (df['descItem'] == 'massa tradicional') | (df['descTipoItem'] =='bebida') | (df['idPedido'] == 0))

df[filtro_massas_bebidas]

#%%
sucos = ['suco de maracujá', 'suco de laranja']
filtro_sucos = df['descItem'].isin(sucos) | (df['descItem'] == 'limonada') 
filtro_sucos
df[filtro_sucos]