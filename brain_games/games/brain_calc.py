from random import randint, choice


CALC_MIN_VALUE = 1
CALC_MAX_VALUE = 1000


RULES = 'What is the result of the expression?'


def get_question_and_answer():
    ran1 = randint(CALC_MIN_VALUE, CALC_MAX_VALUE)
    ran2 = randint(CALC_MIN_VALUE, CALC_MAX_VALUE)
    oper = choice(['+', '*', '-'])
    question_and_answer = (f'{ran1} {oper} {ran2}',
                           str(get_calc(ran1, oper, ran2)))
    return question_and_answer


def get_calc(num1, opeer, num2):
    if opeer == '+':
        return (num1 + num2)
    elif opeer == '-':
        return (num1 - num2)
    elif opeer == '*':
        return (num1 * num2)
