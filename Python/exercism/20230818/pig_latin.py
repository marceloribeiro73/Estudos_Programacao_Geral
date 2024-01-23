'''
    Exercise Pig Latin form Python Track of Exercism
    https://exercism.org/tracks/python/exercises/pig-latin
'''
#%%
def is_vowel(char: str):
    return bool(char.lower() in 'aeiou')

def is_consoant_cluster(text :str):
    return bool(is_vowel(text.lower()[0]) == False and is_vowel(text.lower()[1]) == False)

def translate_word(text :str):
    word_translated = text.lstrip().lower()

    if text.lstrip()[0:2].lower() in ('xr', 'yt') or is_vowel(text.lower().lstrip()[0]) == True:
        word_translated = text.lstrip().lower().rstrip() + 'ay'

    elif is_vowel(text.lstrip()[0]) == False and text.lstrip().lower()[1:3] =='qu' and  text.lstrip().lower()[0:2] != 'qu':
        word_translated =  text.lstrip().lower()[3:] + text.lstrip().lower()[:3] + 'ay'

    elif is_vowel(text.lstrip().lower()[0]) == False and text.lstrip().lower()[1] == 'y' and len(text) == 2:
        word_translated = text.lstrip().lower()[1] + text.lstrip().lower()[0] + 'ay'

    elif is_consoant_cluster(text.lstrip().lower()[0:3]) == True and text.lstrip().lower()[2] == 'y':
        word_translated = text.lstrip().lower().rstrip()[2:] + text.lstrip().lower().rstrip()[0:2] + 'ay'
        
    elif is_consoant_cluster(text.lstrip().lower()[0:3]) and is_vowel(text.lstrip().lower()[2]) == False:
        word_translated = text.lstrip().lower().rstrip()[3:] + text.lstrip().lower().rstrip()[0:3] + 'ay'

    elif is_consoant_cluster(text.lstrip().lower()[0:3]) == True or text.lstrip().lower()[0:2] == 'qu':
        word_translated = text.lstrip().lower().rstrip()[2:] + text.lstrip().lower().rstrip()[0:2] + 'ay'
    
    elif is_vowel(text.lstrip().lower()[0]) == False:
        word_translated = text.lstrip().lower().rstrip()[1:] + text.lstrip().lower().rstrip()[0] + 'ay'
        
    return word_translated


#%%
def translate(sentence :str):
    words_translated = []
    words = sentence.strip().lower().split(sep=' ')
    for word in words:
        words_translated.append(translate_word(word))
    return ' '.join(words_translated)

#%%
#translate(' XRay ')
#is_vowel('a')
#translate('')
#is_consoant_cluster('')

#translate('thrush')

translate("quick fast run")
#%%
text = 'rhythm'
is_consoant_cluster(text.lstrip().lower()[0:3])
# %%
