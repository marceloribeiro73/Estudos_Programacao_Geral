#%%
def square_of_sum(number):
    i = 0
    number_total = 0
    for i in range(1, number+1):
        number_total = number_total + i
    return number_total ** 2


def sum_of_squares(number):
    i = 0
    number_total = 0
    for i in range(1,number+1):
        number_total = number_total + (i **2)
    return number_total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


#%%
#square_of_sum(1)
#sum_of_squares(5)
difference_of_squares(5)
