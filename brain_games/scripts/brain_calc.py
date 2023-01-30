import prompt


from random import randint


from random import choice


def brain_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 1
    while i <= 3:
        x = randint(1,100)
        y = randint(1, 100)
        znak = choice('+-*')
        print(f'Question: {x} {znak} {y}')
        answer = prompt.string('Your answer: ')
        
        if znak == '+':
            real = str(x + y)
            if real == answer:
                print('Correct!')
                i += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer were '{real}'.\nLet's try again, {name}!")
                break
        if znak == '-':
            real = str(x - y)
            if real == answer:
                print('Correct!')
                i += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer were '{real}'.\nLet's try again, {name}!")
                break
        if znak == '*':
            real = str(x * y)
            if real == answer:
                print('Correct!')
                i += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer were '{real}'.\nLet's try again, {name}!")
                break
        
        if i > 3:
            print(f'Congratulations, {name}!')


def main():
    brain_calc()


if __name__ == '__main__':
    main()
