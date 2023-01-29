import prompt


from random import randint 


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        random_number = randint(1,1000)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 == 1 and answer == 'no'):
            i += 1
            print('Correct!')
        if (random_number % 2 == 0 and answer != 'yes'): 
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        if (random_number % 2 == 1 and answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
        if i > 3:
            print(f'Congratulations, {name}!')


def main():
    brain_even()


if __name__ == '__main__':
    main()
