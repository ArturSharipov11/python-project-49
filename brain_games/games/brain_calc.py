from random import randint, choice


from brain_games.engine import MAX_VALUE, MIN_VALUE


RULES = 'What is the result of the expression?'


def get_question_and_answer():
    ran1 = randint(MIN_VALUE, MAX_VALUE)
    ran2 = randint(MIN_VALUE, MAX_VALUE)
    oper = choice(['+', '*', '-'])
    question_and_answer = (f'{ran1} {oper} {ran2}', get_calc(ran1, oper, ran2))
    return question_and_answer


def get_calc(num1, opeer, num2):
    if opeer == '+':
        return str(num1 + num2)
    elif opeer == '-':
        return str(num1 - num2)
    elif opeer == '*':
        return str(num1 * num2)
