#%%
def square(number):
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    grains = 1
    i =0
    for i in range(i+1,number):
        grains += grains
    return grains




def total():
    i = 0
    grains_total =0
    for i in range(i+1, 65):
        grains_total = square(i)
    grains_total += grains_total -1
    return grains_total
    

#%%
square(0)
#%%
total()
# %%

#Exmple using expo
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1

#%%
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return 1 << number - 1


def total():
    return (1 << 64) - 1