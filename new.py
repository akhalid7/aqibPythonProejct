# reads file
def getFileContentAsList(fileName):
    fileContent = []

    # store contents of file + their length in a list
    with open(fileName) as dictionaryFile:
        for line in dictionaryFile:

            # remove \n if it exists at end of our line
            if line[len(line)-1] == '\n':
                line = line[:len(line)-1]

            fileContent.append(line)

    return fileContent

#1
dictionary = getFileContentAsList("dictionary.txt")
possibleDictionary = []
wordLength = 0
guesses = 0

wordFoundWithGivenWordLength = False
shouldDisplayRunningTotalOfWordList = False

#2
while not wordFoundWithGivenWordLength:
    wordLength = raw_input("Enter word length to guess: ")

    if len(wordLength) != 0:
        wordLength = int(wordLength)
        break

    for word in dictionary:
        if len(word) == wordLength:
            wordFoundWithGivenWordLength = True

#3
while guesses <= 0 or guesses > 26:
    guesses = raw_input("Please enter # of guesses: ")

    if len(guesses) != 0:
        guesses = int(guesses)

    if guesses > 0:
        break
    else:
        print("You cannot guess zero or negative # of times or greater then 26")

#4
while shouldDisplayRunningTotalOfWordList:
    pass
shouldDisplayRunningTotalOfWordList = str(raw_input("Do you want to have a running total of the word list? y/n: "))

if (shouldDisplayRunningTotalOfWordList != '' and shouldDisplayRunningTotalOfWordList.lower()[0] == 'y'):
    shouldDisplayRunningTotalOfWordList = 1
else:
    shouldDisplayRunningTotalOfWordList = 0

print("\n")

#5.1: get possible words
for word in dictionary:
    if wordLength == len(word):
        possibleDictionary.append(word)

#5
guessed = []
correctGuesses = {}

for i in range(wordLength):
    correctGuesses[i] = str()
    correctGuesses[i] = "_"

while guesses != 0:
    possibleCategories = {}

    if shouldDisplayRunningTotalOfWordList:
        print("Length of remaining word list: " + str(len(possibleDictionary)))

    print("Word to guess: " + str(correctGuesses.values()))
    print("# of remaining guesses: " + str(guesses))

    guessedChar = str(raw_input("Guess a new character (just one alphabet only): ")).lower()

    # if guessedChar is incorrect in some way ask again!
    if len(guessedChar) > 1 or (ord(guessedChar[0]) < 97 or ord(guessedChar[0]) > 122):
        print("You can only guess an alphabet!")
        continue

    # if guessed then chapair
    if guessedChar in guessed:
        print("You have already guessed this character!")
        print("Your guessed list is: ")
        print(guessed)
        continue

    guessed.append(guessedChar)

    # check where the guessed word occurs for each possible word - this is the word's category
    for word in possibleDictionary:
        wordCategory = []

        # get word's category
        for i in range(len(word)):
            if guessedChar == word[i]:
                wordCategory.append(i)

        # if category already saved then append to it else insert new category
        if tuple(wordCategory) in possibleCategories.keys():
            possibleCategories[tuple(wordCategory)].append(word)
        else:
            possibleCategories[tuple(wordCategory)] = [word]

    # pick the category that has the most words
    biggestWordCategory = max(possibleCategories, key=lambda x:len(set(possibleCategories[x])))

    possibleDictionary = possibleCategories[biggestWordCategory]

    if (biggestWordCategory == ()):
        guesses = guesses - 1
        print("Your guess was not correct\n")
    else:
        for index in biggestWordCategory:
            correctGuesses[index] = guessedChar
        print("Your guess was correct\n")

    if len(possibleDictionary) == 1:
        didWeWin = True

        for ch in correctGuesses.values():
            if ch == '_':
                didWeWin = False
                break

        if didWeWin:
            print("You have guessed the word!!! You win!!!")
            print("The word was:" + str(correctGuesses.values()))
            break
else:
    print("You have run out of guesses.")