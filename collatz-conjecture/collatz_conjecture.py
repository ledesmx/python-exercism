def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    return steps_iterate(number, 0)

def steps_iterate(number, total_steps):
    if number == 1:
        return total_steps

    if number % 2 == 0:
        return steps_iterate(number / 2, total_steps + 1)
    
    return steps_iterate((number * 3) + 1, total_steps + 1)