def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if len(digits) == 1 and digits[0] == 1:
        return [digits[0]]
    if sum(digits) == 0:
        return [0]
    
    if output_base == 10:
        number = base_to_decimal(input_base, digits)
        return [int(num) for num in list(str(number))]
    
    number = base_to_decimal(input_base, digits)
    return decimal_to_base(output_base, number)
     
    
def base_to_decimal(input_base, digits):
    number = 0
    for exponent, digit in enumerate(digits[::-1]):
        number += digit * (input_base ** exponent)
    
    return number

def decimal_to_base(output_base, number):
    exponent = 0
    while (output_base ** exponent) * (output_base - 1) < number:
        exponent += 1
    
    rest = number
    digits = []
    while exponent >= 0:
        multiplier = output_base - 1
        while multiplier > 0:
            current_number = (output_base ** exponent) * multiplier
            if current_number <= rest:
                digits.append(multiplier)
                rest -= current_number
                break
            multiplier -= 1

        if multiplier == 0:
            digits.append(0)
        exponent -= 1

    if len(digits) > 1 and digits[0] == 0:
        return digits[1:]
    
    return digits 
