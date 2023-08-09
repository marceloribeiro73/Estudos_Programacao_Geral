#%%
def is_pangram(sentence : str):
    normalized_sentence = sentence.upper()
    result = True
    alphabet = [chr(word).upper() for word in range(97,123)]
    for i in alphabet[0::]:
        if i not in normalized_sentence:
            print(i)
            result = False
            break
    return result
        
#%%
# alphabet = [chr(word).upper() for word in range(97,123)]
# alphabet

is_pangram("The quick brown fox jumpsover the lazy dog")