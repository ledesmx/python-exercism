def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    sum_of_factors = 0

    for factor in range(1, number):
        if number % factor == 0:
            sum_of_factors += factor

    if sum_of_factors == number:
        return "perfect"
    
    if sum_of_factors < number:
        return "deficient"
    
    return "abundant"
