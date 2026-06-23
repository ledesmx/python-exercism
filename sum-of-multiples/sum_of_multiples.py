def sum_of_multiples(limit, multiples):
    all_multiples = set()
    for base in multiples:
        all_multiples = all_multiples.union(get_multiples(base, limit))
    
    sum_of_multiples = 0
    for number in all_multiples:
        sum_of_multiples += number
    return sum_of_multiples

def get_multiples(base, limit):
    if base == 0:
        return set()
    
    multiples = set()
    number = base
    while number < limit:
        multiples.add(number)
        number += base
    return multiples