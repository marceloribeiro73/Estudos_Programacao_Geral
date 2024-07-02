def get_factors(number):
    end_while = False
    cont = 1
    factors = []
    while cont < number:
        aux = number % cont
        if aux == 0:
            factors.append(cont)
        cont += 1
    return factors


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = get_factors(number)
    sum_fac = 0
    classif = ""
    for n in factors:
        sum_fac += n
    
    if sum_fac == number:
        classif = "perfect"
    elif sum_fac > number:
        classif = "abundant"
    else:
        classif = "deficient"
    return classif



## testes
debug_number = 6
print(get_factors(debug_number))

print(classify(debug_number))
