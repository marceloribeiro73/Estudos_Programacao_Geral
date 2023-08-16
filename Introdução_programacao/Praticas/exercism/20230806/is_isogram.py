#%%
def is_isogram(string: str):
    sentence_normalized = string.lower()
    value_is_isogram = True
    for i in sentence_normalized:
        if not i in '- ':
            if sentence_normalized.count(i) > 1:
                value_is_isogram = False
                break
    return value_is_isogram

#%%
is_isogram('six-year-old')