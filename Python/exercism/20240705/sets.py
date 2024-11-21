"""
    Aprendendo sets
"""

one_element = {1}
print(one_element)

multiple_elements = {1,2,3,44,56,13,32,51,64,71}
print(multiple_elements)

multiple_duplicates = {'Hello!', 'Hello!', 'Hello!',
                            '¡Hola!','Привіт!', 'こんにちは！',
                            '¡Hola!','Привіт!', 'こんにちは！'}
print(multiple_duplicates)

"""
    Set Contructor - set()
"""

no_elements = set()
print(no_elements)

elements_from_tuple = set(("Parrot","Bird",21234,"Bird","Parrot"))
print(elements_from_tuple)

elements_from_list = set([2, 3, 2, 3, 3, 3, 5, 7, 11, 7, 11, 13, 13])
print(elements_from_list)

# String elements (Unicode code points) are
# iterated through and added *individually*.
elements_string = set("Timbuktu")
print(elements_string)

# Unicode separators and positioning code points
# are also added *individually*.
multiple_code_points_string = set('अभ्यास')
print(multiple_code_points_string)