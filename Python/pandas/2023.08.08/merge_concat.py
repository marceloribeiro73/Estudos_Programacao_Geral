#%%
import pandas as pd
# %%
df_item_pedido = pd.read_csv("../example_data/item_pedido.csv")
df_produto = pd.read_csv("../example_data/produto.csv")
df_pedido = pd.read_csv("../example_data/pedido.csv")
# %%
df_join = df_item_pedido.merge(right=df_produto
                                ,how='left')
df_join
# %%
df_join_2 = (df_item_pedido.merge(right=df_produto, how='left')
                            .merge(right=df_pedido[['idPedido','descUF']], how='left'
                            ))
df_join_2
# %%
df_mods = pd.DataFrame(
    {
        "nome" : ["sunny","jv","perry","evaunit73"],
        "idade": [18,27,26,26]
    }
)

df_subs = pd.DataFrame(
    {
        "nome": ["Matheus", "sunny","Maria","kozato"],
        "idade": [32,18,25,29],
        "mesesSub": [1,12,9,10] 
    }
)

(pd.concat([df_mods,df_subs])
    .sort_values(['nome','mesesSub'])
    .drop_duplicates(subset=['nome'])
    .fillna(0)
)