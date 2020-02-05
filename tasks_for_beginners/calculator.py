"""
реализовать калькулятор
пользователь вводит с консоли раздельно операнды и операцию
результат выводится в консоль
результат сохраняется и используется как первый операнд следующей операции
"""

PLUS = '+'
AVAILABLE_OPERATION = (PLUS, '-', '*', '/')
first_number = int(input('enter number 1: '))
while True:
    operation = input('enter operation: ').strip(' ')

    if operation not in AVAILABLE_OPERATION:
        print('operation not available')
        continue

    second_number = int(input('enter number 2: '))
    # result = eval(f"{first_number}{operation}{second_number}")
    result = 0
    if operation == PLUS:
        result = first_number + second_number
    if operation == '-':
        result = first_number - second_number
    if operation == '*':
        result = first_number * second_number
    if operation == '/':
        result = first_number / second_number
    print(f"Result = {result}")
    first_number = result


