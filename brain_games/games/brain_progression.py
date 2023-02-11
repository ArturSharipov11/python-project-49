from random import randint, choice


from brain_games.engine import MIN_VALUE, MAX_VALUE


MIN_LENGTH = 5
MAX_LENGTH = 10
DIFFERENCE = 10
RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    int_term = randint(MIN_VALUE, MAX_VALUE)
    number_of_term = randint(MIN_LENGTH, MAX_LENGTH)
    difference = randint(2, DIFFERENCE)
    string = get_string(int_term, difference, number_of_term)
    num = choice(string)
    index_num = string.index(num)
    string[index_num] = '..'
    string = ' '.join(string)
    question = string
    answer = str(num)
    return question, str(answer)


def get_string(int_term, difference, number_of_term):
    last_char = int_term + difference * number_of_term
    crowd = []
    for i in range(int_term, last_char, difference):
        crowd.append(str(i))
    return crowd
