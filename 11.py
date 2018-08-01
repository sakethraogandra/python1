import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    p=string.ascii_lowercase
    for i in p:
        if i in lettersGuessed:
           location = p.find(i)
           if location != -1:
               p = p[:location] + p[location+1:]
    return p

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
