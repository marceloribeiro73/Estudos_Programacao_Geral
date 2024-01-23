#%%
def colors():
    return [ "black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def color_code(color):
    lst_colors = colors()
    return lst_colors.index(color)
#%%
colors()

color_code("black")