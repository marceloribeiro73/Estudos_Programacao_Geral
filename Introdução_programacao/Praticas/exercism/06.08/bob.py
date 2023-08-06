#%%
def response(hey_bob):
    if hey_bob.isupper() and hey_bob.rstrip()[-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif len(hey_bob) == 0 or hey_bob.isspace() == True:
        return "Fine. Be that way!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.isupper() == False and hey_bob.rstrip()[-1] == '?':
        return "Sure."
    elif  hey_bob.isalpha() == True:
        return "Fine. Be that way!"
    else:
        return "Whatever."
    


#%%
response("Okay if like my  spacebar  quite a bit?   ")