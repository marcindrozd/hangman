import random
from sys import exit

HANGMANPICS = ["""

   +---+
   |   |
       |
       |
       |
       |
       |
===========""", """

   +---+
   |   |
   o   |
       |
       |
       |
       |
===========""", """

   +---+
   |   |
   o   |
   |   |
       |
       |
       |
===========""","""

   +---+
   |   |
   o   |
  /|   |
       |
       |
       |
===========""","""

   +---+
   |   |
   o   |
  /|\  |
       |
       |
       |
===========""","""

   +---+
   |   |
   o   |
  /|\  |
  /    |
       |
       |
===========""","""

   +---+
   |   |
   o   |
  /|\  |
  / \  |
       |
       |
==========="""]

words = """ant baboon badger bat beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose
hawk lioan lizard llama mole monkey moose mouse mule otter owl
panda parrot pigeon python rabbit ram rat raven rhino salmon seal
shark sheep skunk sloth snake spider stork swan tiger turkey turtle
wolf wombat zebra""".split()

missedLetters = ""
correctLetters = ""
alreadyGuessed = ""

def getRandomWord(wordList):
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]
	
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
	print HANGMANPICS[len(missedLetters)]
	print ""
	
	print "Missed letters:",
	for letter in missedLetters:
		print letter,
	print ""
	
	blanks = "_" * len(secretWord)
	
	# change it to something more logical - e.g. something like in Memory
	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
	
	for letter in blanks:
		print letter,
	print ""
	
def getGuess():
	global alreadyGuessed
	while True:
		guess = raw_input("Guess a letter: ")
		guess = guess.lower()
		print alreadyGuessed
		
		if len(guess) != 1:
			print "Please enter a single letter"
		elif guess in alreadyGuessed:
			print "You have already guessed that letter. Please enter another letter."
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print "Please enter a LETTER."
		else:
			alreadyGuessed = alreadyGuessed + guess
			return guess
			
def playAgain():
	print "Do you want to play again?"
	response = raw_input("'yes' or 'no'?: ")
	response = response.lower()
	if response == "yes":
		gameIsDone = False
		missedLetters = ""
		correctLetters = ""
		alreadyGuessed = ""
		gameIsDone = False
		secretWord = getRandomWord(words)
	else:
		exit(1)

gameIsDone = False
print "H A N G M A N"
secretWord = getRandomWord(words)

while gameIsDone == False:
	displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
	guess = getGuess()
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print "Yes! The secret word is '" + secretWord + "'! You have won!"
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess
			
		if len(missedLetters) == len(HANGMANPICS) - 1:
			displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
			print "You have run out of guesses\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses. The word was '" + secretWord + "'"
			gameIsDone = True
			
	if gameIsDone:
		playAgain()
				
	#if gameIsDone:
	#	if playAgain():
	#		missedLetters = ""
	#		correctLetters = ""
	#		alreadyGuessed = ""
	#		gameIsDone = False
	#		secretWord = getRandomWord(words)
	#	else:
	#		break
			
	
		