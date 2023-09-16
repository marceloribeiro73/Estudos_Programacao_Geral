'''
    Exercicio do site https://exercism.org/tracks/python/exercises/raindrops
'''
#%%
def convert(number):
    ''' Convert a number to a string, if the number has 3,5 or 7 as factor, 
        a sound is add to the string, if not, the number itself is returned 
    '''
    string_result =""
    if int(number) % 3 == 0:
        string_result = "".join([string_result,'Pling'])
    if int(number) % 5 == 0:
        string_result = "".join([string_result,'Plang'])
    if int(number) % 7 == 0:
        string_result = "".join([string_result,'Plong'])
    if string_result == "":
        string_result = str(number)
    return string_result

#%%

convert(48)