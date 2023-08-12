
# %%
import pandas as pd
# %%
df = pd.read_csv("../example_data/pedido.csv")
# %%
df.columns
# %%
df.shape
# %%
df.head(20)
# %%
df.dtypes
# %%
df.sample(100)
# %%
df.tail(13)