#%%
def is_valid(isbn):
    isbnWithoutMask = isbn.replace('-','')
    isbnLen = len(isbnWithoutMask)
    if isbnLen != 10:
        print ('Len != 10')
        return False
    else:
        isbnTotal = 0
        for index, digit in enumerate(isbnWithoutMask):
            if digit.isdigit() == True or (index == 9 and (digit == 'X' or digit == 'x')):
                if index == 9 and (digit == 'X' or digit == 'x'):
                    isbnTotal = isbnTotal + (10 * (index + 1))
                else:
                    isbnTotal = isbnTotal + (int(digit) * (index + 1))
            else:
                return False
        
        isbnValidValue = isbnTotal % 11
        if isbnValidValue == 0:
            return True
        else:
            return False

#%%
is_valid("3-598-21508-8")

