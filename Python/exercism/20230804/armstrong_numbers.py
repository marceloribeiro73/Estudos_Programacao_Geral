#%%
def is_armstrong_number(number):
    number_string = str(number)
    number_len = len(number_string)
    number_total =0
    for digit in (number_string):
        number_total = number_total + (int(digit) ** number_len)
    if number == number_total:
        return True
    else:
        return False

#%%
is_armstrong_number(154)