#%%
def steps(number):
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    else:
        count_steps = 0
        number_product = number
        while(number_product != 1):
            if number_product % 2 == 0:
                number_product = number_product/2
                count_steps +=1
            else:
                number_product = (number_product*3)+1
                count_steps +=1
        return count_steps 

#%%
steps(1578596)