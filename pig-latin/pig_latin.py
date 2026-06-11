def translate(text):
    text_list = text.rsplit(" ")
    final_translation = ""
    for word in text_list:
        final_translation += " " + translate_word(word)
    
    return final_translation.lstrip()

def translate_word(word):
    if len(word) > 1:
        if is_vowel(word[0]) or is_xr_or_yt(word[0] + word[1]):
            return word + "ay"
        
        qu_index = index_of_qu(word)
        if qu_index > 0:
            return word[qu_index + 1:] + word[:qu_index + 1] + "ay"
        
        y_index = index_of_y(word)
        if y_index > 0:
            return word[y_index:] + word[:y_index] + "ay"
        
        return word[index_of_vowel(word):] + word[:index_of_vowel(word)] + "ay"

    return word

def is_vowel(letter):
    return letter in {"a", "e", "i", "o", "u"}

def is_xr_or_yt(letters):
    return letters in {"xr", "yt"}

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

        
