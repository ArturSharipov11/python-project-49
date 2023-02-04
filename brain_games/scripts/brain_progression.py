import prompt


from random import randint


from random import choice


import math


def brain_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    index = 1
    while index <= 3:
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
        print(f"Question: {string}")
        answer = prompt.string('Your answer: ')
        if answer == str(num):
             print('Correct!')
             index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer were '{num}'.\nLet's try again, {name}!")
            break
        if index > 3:
            print(f"Congratulations, {name}!")


def main():
    brain_progression()


if __name__ == '__main__':
    main()
