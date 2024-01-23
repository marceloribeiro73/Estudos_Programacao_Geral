
# %%
import pandas as pd
import matplotlib as plt
# %%
df = pd.read_csv("../example_data/produto.csv")
df
# %%
df["vlPreco"].describe()
# %%
df['vlPrecoAjuste1'] = (df["vlPreco"] * 1.12).round(2)
df.describe()
# %%
df['descItemPrimeiro'] = df['descItem'].apply(lambda x: x.lower().split(" ")[0])
df[['descItem','descItemPrimeiro']].describe()
# %%
freq = pd.value_counts(df['descItemPrimeiro'])
freq
# %%
df.groupby(by=['descItemPrimeiro'])[['vlPreco','vlPrecoAjuste1']].mean()
# %%
(df.groupby(by=['descItemPrimeiro'])[['vlPreco','vlPrecoAjuste1']]
    .agg(['min','mean','max','median']))