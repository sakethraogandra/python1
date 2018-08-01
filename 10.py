def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    a=""
    for i in secretWord:
        if i not in lettersGuessed:
           a=a+"_"
        else:
             a=a+i
    return a
secretWord='apple'
lettersGuessed=['e','i','k','p','r','s']
print(isWordGuessed(secretWord, lettersGuessed))

