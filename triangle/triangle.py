# An equilateral triangle has all three sides the same length.
def equilateral(sides):
    if not is_a_triangle(sides):
        return False
    
    return sides[0] == sides[1] == sides[2]


# An isosceles triangle has at least two sides the same length. 
# (It is sometimes specified as having exactly two sides the same 
#  length, but for the purposes of this exercise we'll say at least two.)
def isosceles(sides):
    if not is_a_triangle(sides):
        return False
    
    if sides[0] == sides[1]:
        return True

    if sides[0] == sides[2]:
        return True

    if sides[1] == sides[2]:
        return True
    
    return False


# A scalene triangle has all sides of different lengths.
def scalene(sides):
    if not is_a_triangle(sides):
        return False
    
    if sides[0] == sides[1]:
        return False

    if sides[0] == sides[2]:
        return False

    if sides[1] == sides[2]:
        return False
    
    return True

# Note
# For a shape to be a triangle at all, all sides have to be of length > 0,
# and the sum of the lengths of any two sides must be greater than or 
# equal to the length of the third side.
def is_a_triangle(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    if sides[0] + sides[1] < sides[2]:
        return False
    if sides[0] + sides[2] < sides[1]:
        return False
    if sides[1] + sides[2] < sides[0]:
        return False
    
    return True
