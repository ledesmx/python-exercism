def is_armstrong_number(number):
    sum_of_digits = 0
    digits = [int(digit) for digit in str(number)]
    exponent = len(digits)
    for digit in digits:
        sum_of_digits += digit ** exponent

    return sum_of_digits == number