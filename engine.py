import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.rules)
    index = 1
    while index <= 3:
        (question, answer) = game.question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
        if index > 3:
            print(f"Congratulations, {name}!"
