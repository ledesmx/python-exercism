def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    
    # Four bands
    if len(colors) == 4:
        code1 = get_code(colors[0])
        code2 = get_code(colors[1])
        code3 = get_code(colors[2])

        code_with_zeros = add_zeros(code1 + code2, int(code3))
        code = clean_and_add_metric(code_with_zeros)
        return code + get_tolerance(colors[3])
    
    # Five bands
    code1 = get_code(colors[0])
    code2 = get_code(colors[1])
    code3 = get_code(colors[2])
    code4 = get_code(colors[3])

    code_with_zeros = add_zeros(code1 + code2 + code3, int(code4))
    code = clean_and_add_metric(code_with_zeros)
    return code + get_tolerance(colors[4])


def add_zeros(str_code, multiplier):
    zeros = {
        0: "",
        1: "0",
        2: "00",
        3: "000",
        4: "0000",
        5: "00000",
        6: "000000",
        7: "0000000",
        8: "00000000",
        9: "000000000",
    }
    return str_code + zeros.get(multiplier)

def clean_and_add_metric(code):
    # Megaohms
    if len(code) == 9:
        clean_code = remove_extra_zeros(code[:3] + "." + code[3:])
        return clean_code.rstrip(".") + " megaohms"
    if len(code) == 8:
        clean_code = remove_extra_zeros(code[:2] + "." + code[2:])
        return clean_code.rstrip(".") + " megaohms"
    if len(code) == 7:
        clean_code = remove_extra_zeros(code[:1] + "." + code[1:])
        return clean_code.rstrip(".") + " megaohms"
    
    # Kiloohms
    if len(code) == 6:
        clean_code = remove_extra_zeros(code[:3] + "." + code[3:])
        return clean_code.rstrip(".") + " kiloohms"
    if len(code) == 5:
        clean_code = remove_extra_zeros(code[:2] + "." + code[2:])
        return clean_code.rstrip(".") + " kiloohms"

    if len(code) == 4:
        clean_code = remove_extra_zeros(code[:1] + "." + code[1:])
        return clean_code.rstrip(".") + " kiloohms"

    
    # Ohms
    return code + " ohms"

def remove_extra_zeros(code):
    reversed_code = code[::-1]
    cut_at = 0
    for index, number in enumerate(reversed_code):
        cut_at = index
        if number != "0" or number == ".":
            break
    
    if cut_at == 0:
        return code
    
    return code[:-cut_at]

def get_tolerance(color):
    tolerance_map = {
        "grey": " ±0.05%",
        "violet": " ±0.1%",
        "blue": " ±0.25%",
        "green": " ±0.5%",
        "brown": " ±1%",
        "red": " ±2%",
        "gold": " ±5%",
        "silver": " ±10%",
    }
    return tolerance_map.get(color)

def get_code(color):
    code_map = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }
    return code_map.get(color)
