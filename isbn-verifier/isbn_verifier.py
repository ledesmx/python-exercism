def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) != 10:
        return False
    
    isbn_list = list(clean_isbn)
    isbn_list.reverse()

    
    sum_of_digits = 0
    for index, number in enumerate(isbn_list):
        digit = 0
        if number == "X" and index == 0:
            digit = 10
        else:
            if number.isdigit():
                digit = int(number)
            else:
                return False
        sum_of_digits += digit * (index + 1)
    
    return sum_of_digits % 11 == 0
