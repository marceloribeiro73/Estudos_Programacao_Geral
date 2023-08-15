#%%
import pandas as pd
# %%
pd.set_option('display.max_rows', 100)
df_produto = pd.read_csv("../example_data/produto.csv")
#%%
df_produto["primeiroNome"] = df_produto['descItem'].apply(lambda x: x.lower().split(" ")[0])
# %%
df_produto = df_produto.sort_values(
    by=['vlPreco','descItem'],
    ascending=[False, True]
)
df_produto
# %%
df_produto.drop_duplicates(subset=['primeiroNome'],keep='first')