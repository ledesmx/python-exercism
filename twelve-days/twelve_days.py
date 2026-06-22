def recite(start_verse, end_verse):
    day = (
        "first day",
        "second day",
        "third day",
        "fourth day",
        "fifth day",
        "sixth day",
        "seventh day",
        "eighth day",
        "ninth day",
        "tenth day",
        "eleventh day",
        "twelfth day"
    )
    
    lyrics = []
    for index in range(start_verse - 1, end_verse):
        lyrics.append("On the " + day[index] + " of Christmas my true love gave to me: " + get_gifts(index + 1))

    return lyrics

def get_gifts(day):
    gift_lyric = (
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    )
    gifts = ""
    for index_day in range(day, 0, -1):
        gifts += gift_lyric[index_day - 1]
        if index_day == 1:
            gifts += "."
        elif index_day == 2:
            gifts += ", and "
        else:
            gifts += ", "
    
    return gifts
