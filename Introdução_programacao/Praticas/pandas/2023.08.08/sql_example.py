#%%
import pandas as pd
import sqlalchemy as sqla

# %%
'''função para importar um arquivo .sql 
para separar as querry do codigo python'''
def import_query(path: str):
    with open(path,'r') as open_file:
        query = open_file.read()
    return query

# %%
engine = sqla.create_engine("sqllite:///../example_data/database.db")

# %%
query = import_query('example.sql')
print(query)

# %%
df_query = pd.read_sql_query(query, engine)
df_query


# %%
import datetime

top5_uf = (df_query.sort_values("qtdePedido", ascending=False)
                           .head(5))

top5_uf['dt_ingestao'] = datetime.datetime.now()

top5_uf.to_sql('top5_uf_pedido', engine, if_exists='append')