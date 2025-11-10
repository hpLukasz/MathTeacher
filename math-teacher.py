#!/usr/bin/env python3

import random
import sys

dividend = [4, 6, 8, 9, 10, 12, 14, 16, 18, 20, 21, 24, 27, 28, 30, 32, 36, 40, 42, 48, 49, 50, 54, 56, 60, 64, 70, 72, 80, 81, 90, 100]
divisor =  [[2, 3, 4, 3, 5,  6,  7,  8,  9,  10, 7,  8,  9,  7,  10, 8,  9,  4,  7,  8,  7,  5,  9,  8,  6,  8,  7,  8,  8,  9,  9,  10],
            [4, 2, 2, 3, 2,  2,  2,  2,  2,  2,  3,  3,  3,  4,  3,  4,  4,  10, 6,  6,  7,  10, 6,  7,  10, 8,  10, 9,  10, 9,  10, 25]]

class Operation:
    def __init__(self, num1, num2, operation, correct_result):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        self.correct_result = correct_result

    def __eq__(self, other_operation):
        if not isinstance(other_operation, Operation):
            raise TypeError('Can only compare two operations')
        if  (self.num1 == other_operation.num1 and \
            self.num2 == other_operation.num2 and \
            self.correct_result == other_operation.correct_result) or \
            (self.num1 == other_operation.correct_result and
             (self.num2 == other_operation.num1 or
             self.num2 == other_operation.num2)) or \
            (self.correct_result == other_operation.num2 and
             (self.num2 == other_operation.num1 or
             self.num2 == other_operation.num2)):
            return True
        else:
            return False

def give_evaluation(score):
    evaluation = sum(score)
    if evaluation >= 9:
        return "6"
    elif evaluation >= 7 and evaluation < 9:
        return "5"
    elif evaluation >= 5 and evaluation < 7:
        return "4"
    elif evaluation >= 3 and evaluation < 5:
        return "3"
    elif evaluation >= 1 and evaluation < 4:
        return "2"
    else:
        return "1"

def give_operation():
    operation = random.choice(['*', ':'])
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    correct_result = 0

    if operation == '*':
        correct_result = num1 * num2
    else:
        # num1 = random.randint(1, 100)
        # num2 = random.randint(2, 9)
        # while num1 % num2 != 0:  # Ensure division results in an integer
        #     num1 = random.randint(1, 100)
        #     num2 = random.randint(2, 9)
        # correct_result = num1 / num2
        idx = random.randint(0, 31)
        divisor_idx = random.randint(0, 1)
        num1 = dividend[idx]
        num2 = divisor[divisor_idx][idx]
        correct_result = num1 / num2

    return Operation(num1, num2, operation, correct_result)
 
 
if len(sys.argv) > 1:
    noMathOperations = int(sys.argv[1])
else:
    noMathOperations = 10
customerResults = [None] * noMathOperations

for i in range(noMathOperations):
    all_operations = []

    operation = give_operation()
    while operation in all_operations:
        operation = give_operation()
    all_operations.append(operation)

    print(f"{i+1}\nJaki wynik: {operation.num1} {operation.operation} {operation.num2}?")
    user_answer_str = input("Twoja odpowiedz: ")
    if user_answer_str.isdigit():
        user_answer = int(user_answer_str)
    else:
        user_answer = 0

    if user_answer == operation.correct_result:
        print("DOBRZE!")
        customerResults[i] = True
    else:
        print(f"ZLE! Poprawna odpowiedz to: {int(operation.correct_result)}.")
        customerResults[i] = False

print("\nPodsumowanie wyników:")
for i, result in enumerate(customerResults):
    status = "DOBRZE" if result else "ZLE"
    print(f"Zadanie {i + 1}: {status}")


print("Ocena końcowa: ", give_evaluation(customerResults))