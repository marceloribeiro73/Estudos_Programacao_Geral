def encode(plain_text: str):
    LATIM_ALPHABET = "-abcdefghijklmnopqrstuvwxyz"
    chiper = ""
    grp_count = 0
    for letter in plain_text:
        position = LATIM_ALPHABET.find(letter.lower()) 
        #print(str(position) + " " + str(LATIM_ALPHABET[position*-1]))
        if position > 0:
            chiper = chiper + LATIM_ALPHABET[position*-1]
            grp_count += 1
            if (grp_count % 5) == 0:
                chiper += " " 
        if letter.isdigit():
            chiper = chiper + letter
            grp_count += 1
            if (grp_count % 5) == 0:
                chiper += " " 
    return chiper.rstrip(" ")


def decode(ciphered_text):
    CIPHER_ALPHABET = "-zyxwvutsrqponmlkjihgfedcba"
    chiper = ""
    for letter in ciphered_text:
        position = CIPHER_ALPHABET.find(letter.lower()) 
        #print(str(position) + " " + str(LATIM_ALPHABET[position*-1]))
        if position > 0:
            chiper = chiper + CIPHER_ALPHABET[position*-1]
        if letter.isdigit():
            chiper = chiper + letter
    return chiper

print(encode("The quick brown fox jumps over the lazy dog."))
# print(encode("test"))
# print(encode("x123 yes"))
# print(decode("gvhg"))
# print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))
