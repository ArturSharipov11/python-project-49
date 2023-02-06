from random import randint, choice


rules = 'What number is missing in the progression?'


def question_and_answer():
    string = []
    x = randint(5, 10)
    y = randint(1, 20)
    a = randint(2, 7)
    stop = y + (x * a)
    for i in range(y, stop, a):
        string.append(str(i))
    num = choice(string)
    index_num = string.index(num)
    string[index_num] = '..'
    string = ' '.join(string)
    question = string
    answer = str(num)
