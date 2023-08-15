
# %%
import pandas as pd

#%%

df = pd.read_csv('../example_data/produto.csv')
df

# %%
df['precoMax'] = (df['vlPreco'] * 2.50).round(2)
df
# %%
def ajuste_valor(valor):
    saida =0
    if valor <= 1:
        saida = valor * 1.01
    elif valor <= 7.50:
        saida = valor * 1.005
    else:
        saida = valor * 1.09
    return saida
#%%
df['vlPrecoAjustado'] =df["vlPreco"].apply( ajuste_valor ).round(2)

#%%

df