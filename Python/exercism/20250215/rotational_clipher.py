def rotate(text: str, key: int):
    LATIM_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for letter in text:
      flag_upper_case = letter.isupper()
      position = LATIM_ALPHABET.find(letter.lower())
      if position == -1:
        cipher = cipher + letter
      else:
        nPosition = int(position) + int(key)
        if nPosition >= 26:
           nPosition = nPosition - 26
        if flag_upper_case:
           cipher = cipher + LATIM_ALPHABET[nPosition].upper()
        else:
           cipher = cipher + LATIM_ALPHABET[nPosition]
    return cipher


print(rotate("Testing 1 2 3 testing","4"))