import random

def get_random_code():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!@#$%^&*()-=_+[]{}"
    code = ""
    for i in range(10):
        code += random.choice(letters)
        code += random.choice(numbers)
        code += random.choice(symbols)
    return code
