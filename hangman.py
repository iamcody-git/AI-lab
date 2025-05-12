import random
words = ['nepal', 'pokhara', 'kathmandu', 'dumkibas']
word = random.choice(words)
print('Guess the charater')
guessed_word =''
chances = 12
while chances > 0:
    failed=0
    for char in word:
        if char in guessed_word:
            print(char, end='')
        else:
            print("_", end='')
            failed +=1
            
    if failed == 0:
        print('\n')
        print("You win")
        print("The word is: ", word + '.')
        break
    print('\n')
    guess = input('Guess a character:')
    guessed_word += guess
    if guess not in word:
        chances -= 1
        print("Wrong")
        print("You have", chances, 'more guesses.')
        if chances == 0:
            print('You lose.')
        