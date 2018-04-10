print('Guess my number between 0 and 100!')
low = 0
high = 100
ans = (low + high) // 2
Guessing = True

while Guessing:
    Guess = input('Is your secret number ' + str(ans) + '? Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')

    if Guess == 'h':
        high = ans
    elif Guess == 'l':
        low = ans
    elif Guess == 'c':
        print('You guessed correctly!')
        Guessing = False
    ans = (low + high) // 2
