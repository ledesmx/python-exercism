def roman(number):
    roman_number = ""
    rest = number
    values = (
        (1000, 1000, "M"),
        (500, 100, "D"),
        (100, 100, "C"),
        (50, 10, "L"),
        (10, 10, "X"),
        (5, 1, "V"),
        (1, 1, "I"),
    )
    for index, value in enumerate(values):
        if rest // value[0]:
            multiplier = rest // value[1]
            if multiplier >= 5:
                if multiplier == 9:
                    roman_number += values[index + 1][2] + values[index - 1][2]
                else:
                    roman_number += values[index][2] + (values[index + 1][2] * (multiplier - 5))
            else:
                if multiplier == 4:
                    roman_number += values[index][2] + values[index - 1][2]
                else:
                    roman_number += values[index][2] * multiplier
            rest -= multiplier * value[1]
    
    return roman_number
