import string
from collections import deque

# http://www.cs.nthu.edu.tw/~wkhon/ds/ds10/tutorial/tutorial2.pdf

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def power(a, b):
    return a ** b

def convert_postfix(numbers):
    chars_list = resize_operators([x for x in numbers])
    one_number = ''
    new_list = []
    t = 0
    if chars_list:
        for x in chars_list:
            if x not in '+-/*()^':
                one_number += x
                t += 1
                if t == len(chars_list):
                    if one_number != '':
                        new_list.append(one_number)
            else:
                if one_number != '':
                    new_list.append(one_number)
                one_number = ''
                new_list.append(x)
                t += 1
        operands = []
        operators = []
        prec = {'(': 4, '^':3, '*': 2, '/': 2, '+': 1, '-': 1}
        for x in new_list:
            if x not in '+-/*()^':
                operands.append(x)
                while x == new_list[-1] and len(operators) != 0:
                    operands.append(operators.pop())
            else:
                if len(operators) == 0 or operators[-1] == '(':
                    operators.append(x)
                elif x == ')':
                    if '(' not in operators:
                        print('Invalid expression 1')
                        return False
                    else:
                        while operators[-1] != '(':
                            operands.append(operators.pop())
                        operators.pop()
                elif prec[x] > prec[operators[-1]]:
                    operators.append(x)
                elif prec[x] <= prec[operators[-1]]:
                    while prec[x] <= prec[operators[-1]]:
                        operands.append(operators.pop())
                        if len(operators) == 0:
                            break
                    operators.append(x)
        if '(' in operands:
            print('Invalid expression 2')
            return False
        else:
            while len(operators) != 0:
                operands.append(operators.pop())
        return operands

def convert_answer(numbers):
    postfix = numbers
    result = []
    if postfix != None:
        for x in postfix:
            if x not in '^*/+-':
                if check_dict(x):
                    result.append(vars_dict[x])
                else:
                    result.append(int(x))
            else:
                if x == '^':
                    result.append(power(result.pop(-2), result.pop()))
                elif x == '*':
                    result.append(multiplication(result.pop(-2), result.pop()))
                elif x == '/':
                    result.append(division(result.pop(-2), result.pop()))
                elif x == '+':
                    result.append(addition(result.pop(-2), result.pop()))
                elif x == '-':
                    result.append(substraction(result.pop(-2), result.pop()))
        return result

def get_numbers(numbers):
    operators = [x for x in numbers if x.startswith('+') or (x.startswith('-') and len(x) == 1)]
    values = [x for x in numbers if x not in ['+', '-']]
    final_values = []
    dict_values = [vars_dict[x] for x in numbers if check_dict(x)]
    for x in values:
        if check_dict(x):
            final_values.append(vars_dict[x])
        else:
            final_values.append(int(x))
    return final_values, operators

def operation(numbers):
    if resize_operators(numbers):
        val, op = get_numbers(numbers)
        if len(op) == 0 and len(val) > 1:
            return 'Invalid expression 3'
        else:
            total = val[0]
            val.pop(0)
            for x, y in zip(val, op):
                # print(x, y)
                if y == '+':
                    total = addition(total, x)
                elif y == '-':
                    total = substraction(total, x)
            return total

def resize_operators(numbers):
    new_numbers = []
    for x in numbers:
        if x == ' ':
            continue
        if x not in '+-/*':
            new_numbers.append(x)
        elif x in '+':
            if new_numbers[-1] != x:
                new_numbers.append(x)
        elif x in '/*':
            if new_numbers[-1] != x:
                new_numbers.append(x)
            elif new_numbers[-1] == x:
                print('Invalid expression')
                return False
        elif x == '-':
            if new_numbers[-1] == '-':
                new_numbers.pop()
                new_numbers.append('+')
            elif new_numbers[-1] == '+':
                new_numbers.pop()
                new_numbers.append('-')
            else:
                new_numbers.append(x)
    return new_numbers

vars_dict = {}
az = list(string.ascii_letters)
zeronine = list(string.digits)

def check_dict(x):
    return True if (vars_dict.get(x) or vars_dict.get(x) == 0) else False

def check_variable(x):
    testaz = [y for y in x if y in az]
    return True if len(x) == len(testaz) else False

def create_variables(a, b):
    try:
        if check_dict(b):
            b = vars_dict[b]
        vars_dict[a] = int(b)
    except ValueError:
        if check_variable(b):
            print('Unknown variable')
        else:
            print('Invalid asignment')

while True:
    numbers = input()
    if '=' in numbers:
        if numbers.count('=') > 1:
            print('Invalid asignment')
        else:
            numbers = numbers.split('=')
            if check_variable(numbers[0].strip()):
                create_variables(numbers[0].strip(), numbers[1].strip())
            else:
                print('Invalid identifier')
    else:
        if len(numbers) == 0:
            continue
        if numbers.startswith('/'):
            if numbers in ['/help', '/exit']:
                if numbers == '/help':
                    print('The program can calculate addition and substraction \
                     of multiple numbers and can also store variables.')
                elif numbers == '/exit':
                    print('Bye!')
                    break
            else:
                print('Unknown command')

        elif len(numbers.strip().split()) == 1:
            if check_variable(numbers.strip()[0]):
                if check_dict(numbers.strip()[0]):
                    print(vars_dict[numbers.strip()[0]])
                else:
                    print('Unknown variable')
            else:
                print('Invalid identifier')
        else:
            test = convert_postfix(numbers)
            if test != False:
                result = convert_answer(test)
                if result:
                    print(round(result[0]))
