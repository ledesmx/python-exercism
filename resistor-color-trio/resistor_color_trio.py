def label(colors):
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
    metric_map = {
        0: " ohms",
        1: "0 ohms",
        2: "00 ohms",
        3: " kiloohms",
        4: "0 kiloohms",
        5: "00 kiloohms",
        6: " megaohms",
        7: "0 megaohms",
        8: "00 megaohms",
        9: " gigaohms",
    }
    code1 = code_map.get(colors[0])
    code2 = code_map.get(colors[1])
    code3 = code_map.get(colors[2])

    if code1 == code2 == code_map.get("black"):
        return "0 ohms"
    
    if code2 == code_map.get("black"):
        return code1 + metric_map.get(1 + int(code3))
    
    numbers = ""
    if code1 == code_map.get("black"):
        numbers = code2
    else:
        numbers = code1 + code2

    return numbers + metric_map.get(int(code3))
    