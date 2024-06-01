from typing import List


def hello(name: str = None) -> str:
    if name:
        return "Hello, " + name + "!"
    return "Hello!"


def int_to_roman(num: int) -> str:
    d = {   
            1000 : "M",
            900  : "CM",
            500  : "D",
            400  : "CD",
            100  : "C",
            90   : "XC",
            50   : "L",
            40   : "XL",
            10   : "X",
            9    : "IX",
            5    : "V",
            4    : "IV",
            1    : "I"
        }
    result = ""
    while num:
        for numeral in d:
            if num >= numeral:
                result += d[numeral]
                num -= numeral
                break
    return result


def longest_common_prefix(strs_input: List[str]) -> str:
    if (strs_input == None) or (len(strs_input) == 0):
        return ""
    prefix = strs_input[0].strip()
    length = len(prefix)
    for i in range (length, 0, -1):
        flag = True
        for string in strs_input:
            string = string.strip()
            for j in range(i):
                if string[j] != prefix[j] or i > len(string):
                    flag = False
                    break
        if flag:
            return prefix[:i]
    return ''
    

def is_prime(num):
    for k in range (2, int(pow(num, 0.5)) + 1):
        if num % k == 0:
            return False
    return True


def primes() -> int:
    p = 2
    while True:
        if is_prime(p):
            yield p
        p += 1


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = -1):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__ (self, sum_spent):
        if (sum_spent > self.total_sum):
            raise ValueError("Not enough money to spend ", sum_spent, " dollars.")
        self.total_sum -= sum_spent
        return "You spent " + str(sum_spent) + " dollars."

    def __repr__(self):
        return "To learn the balance call balance."

    @property
    def balance(self):
        if (self.balance_limit != 0):
            if (self.balance_limit != -1):
                self.balance_limit -= 1
            return self.total_sum
        else:
            raise ValueError("Balance check limits exceeded.")
        
    
    def put(self, sum_put):
        self.total_sum += sum_put
        print("You put ", sum_put, " dollars.")

    def __add__ (self, b):
        self.total_sum += b.total_sum
        self.balance_limit = max(self.balance_limit, b.balance_limit)
        return self
