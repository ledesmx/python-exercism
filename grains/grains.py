def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    grains = 1
    for square in range(1, number):
        grains *= 2
    
    return grains


def total():
    total = 1
    grains = 1
    for square in range(1, 64):
        grains *= 2
        total += grains

    return total
