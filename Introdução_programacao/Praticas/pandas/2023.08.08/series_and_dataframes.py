#%% 

import pandas as pd

# %%

pontos = [10,20,12,9,2,15,22,15,23,54,23]

#%%

serie_pontos = pd.Series(pontos)

#%%
contagem_pontos = serie_pontos.count()
contagem_pontos


# %%
media_pontos = serie_pontos.mean()
media_pontos

# %%
mediana_pontos = serie_pontos.median()
mediana_pontos
# %%
desvioPad_pontos = serie_pontos.std()
desvioPad_pontos
# %%
desc_pontos = serie_pontos.describe()
desc_pontos