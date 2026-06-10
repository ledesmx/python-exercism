def is_armstrong_number(number):
    sum = 0
    digits = [int(d) for d in str(number)]
    exponent = len(digits)
    for digit in digits:
        sum += digit ** exponent

    return sum == number