# Calculator business logic module

def Calculator(a, b, operations):
    if operations == 'add':
        return a + b
    elif operations == 'sub':
        return a - b
    elif operations == 'mul':
        return a * b
    elif operations == 'div':
        if b != 0:
            return a / b
        else:
            return 'error: division by zero'
    else:
        return 'Error: Invalid operation'


    