#%%
import pandas as pd
#%%
sorteios = pd.read_csv("data/mega_sorteios.csv", sep=";", index_col="Concurso")

#%%
sorteios.head(100)
#%%
numeros_entrada == [12,23,43,56,27,2]
#%%
sorteios.loc[(sorteios['bola 1'] == 7) & 
    (sorteios['bola 2'] == 22) &
    (sorteios['bola 3'] == 34) &
    (sorteios['bola 4'] == 34) &
    (sorteios['bola 5'] == 34) &
    (sorteios['bola 6'] == 34)] 
#%%
sorteios.groupby(['bola 1'])['Concurso'].count()