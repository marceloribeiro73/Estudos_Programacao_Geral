def square_root(number):
    sqr_result = 0
    if number == 1:
        sqr_result = 1
    elif number > 1:
        amt_ops = 0
        subtr_number = 1
        while number > 0:
            number -= subtr_number
            amt_ops += 1
            subtr_number += 2
        sqr_result = amt_ops
    return sqr_result

print(square_root(1024))