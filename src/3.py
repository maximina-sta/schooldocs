def get_random_python_code():
    # Generate a random number between 1 and 100
    num = randint(1, 100)

    # If the number is even, return a string
    if num % 2 == 0:
        return "print('Hello, world!')"

    # If the number is odd, return a list of numbers
    else:
        return [i for i in range(num)]
