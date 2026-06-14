def score(x, y):
    distance_from_center = ((x ** 2) + (y ** 2)) ** 0.5

    if distance_from_center > 10:
        return 0
    
    if distance_from_center > 5:
        return 1
    
    if distance_from_center > 1:
        return 5
    
    return 10
