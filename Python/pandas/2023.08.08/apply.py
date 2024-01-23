
# %%
import pandas as pd
# %%
df_produto = pd.read_csv("../example_data/produto.csv")
df_produto
# %%
def is_massa(x):
    return x.lower().startswith('massa')
# %%
df_produto['flMassa'] = df_produto["descItem"].apply(is_massa)
df_produto[df_produto['flMassa']]
# %%
df_produto["descItem"].apply(lambda x : x.lower().startswith('massa'))
# %%
df_produto["descItem"].str.lower().str.startswith('massa')