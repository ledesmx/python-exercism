def is_pangram(sentence):
    letters = sentence.replace(" ", "").casefold()
    set_of_letters = set([])
    for letter in letters:
        if letter in {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}:
            set_of_letters.add(letter)
    
    if len(set_of_letters) == 26:
        return True
    
    return False
