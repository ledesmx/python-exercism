class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if not self.card_num.isdecimal():
            return False
        if len(self.card_num) <= 1:
            return False
        numbers = list(self.card_num)
        numbers.reverse()
        sumof = 0
        for index, number in enumerate(numbers):
            num = int(number)
            if (index + 1) % 2 == 0:
                double = num * 2
                if double > 9:
                    double -= 9
                sumof += double
            else:
                sumof += num
        
        if sumof % 10 == 0:
            return True
        
        return False
