def translate(text):
    if len(text) > 1:
        new_word = ""

        if is_vowel(text[0]) or is_xr_or_yt(text[0] + text[1]):
            return text + "ay"
        
        qu_index = index_of_qu(text)
        if qu_index > 0:
            return text[qu_index + 1:] + text[:qu_index + 1] + "ay"
        
        y_index = index_of_y(text)
        if y_index > 0:
            return text[y_index:] + text[:y_index] + "ay"
        
        return text[index_of_vowel(text):] + "ay"

    return text

def is_vowel(letter):
    return letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"

def is_xr_or_yt(letters):
    return letters == "xr" or letters == "yt"

def index_of_vowel(text):
    for index, letter in enumerate(text):
        if is_vowel(letter):
            return index
        
    return -1

def index_of_qu(text):
    for index, letter in enumerate(text):
        if is_vowel(letter):
            return -1
        
        if letter == "q" and len(text) > index + 1:
            if text[index + 1] == "u":
                return index + 1

    return -1

def index_of_y(text):
    for index, letter in enumerate(text):
        if is_vowel(letter):
            return -1
        
        if letter == "y":
            return index

    return -1

        
