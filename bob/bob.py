def response(hey_bob):
    clean_hey_bob = hey_bob.strip()

    if clean_hey_bob == "":
        return "Fine. Be that way!"

    if clean_hey_bob[-1] == "?" and clean_hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    
    if clean_hey_bob[-1] == "?":
        return "Sure."
    
    if clean_hey_bob.isupper():
        return "Whoa, chill out!"
    
    return "Whatever."
