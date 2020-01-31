"""
реализовать калькулятор с польской нотацией
1 5 6 + - = 10
\6 5 a b - -> 6 - 5= a -b
пользователь вводит с консоли раздельно операнды и операцию, оператды сохраняются в стек
результат сохраняется в стек и используется как первый операнд следующей операции
при вводе с консоли "=" выпводится (но не удаляется) верхний элемент стека
"""

AVAILABLE_OPERATION = ('+', '-', '*', '/', '=')
stack = []

while True:
    print('=', stack)
    c = input('number or operation: ').strip(' ')
    if c in AVAILABLE_OPERATION:
        if c == '=':
            if len(stack) > 0:
                result = stack.pop()
                stack.append(result)
                print(result)
            else:
                print('Stack is empty')
            continue
        if len(stack) > 1:
            second_number, first_number = stack.pop(), stack.pop()
            if c == '+':
                stack.append(first_number + second_number)
            if c == '-':
                stack.append(first_number - second_number)
            if c == '*':
                stack.append(first_number * second_number)
            if c == '/':
                if second_number == 0:
                    print('Second operand is zero')
                    stack.append(first_number)
                    stack.append(second_number)
                else:
                    stack.append(first_number / second_number)
        else:
            print('Stack contain > 1')
        continue
    else:
        stack.append(int(c))
