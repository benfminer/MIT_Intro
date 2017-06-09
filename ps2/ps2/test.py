secret_word = 'test'
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    letters_guessed = []
    print('Welcome to the game of Hangman!')
    print('I am thinking of a word that is ', len(secret_word), ' letters long')
    print('----------')

    while guesses_left >= 0 or is_word_guessed(secret_word, letters_guessed):
        print('You have ', guesses_left, 'left.')
        print('Available letters : ', get_available_letters(letters_guessed))
        break


letter = 'c'
print(letter.isalpha())
