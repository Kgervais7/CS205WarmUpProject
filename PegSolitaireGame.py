from englishPeg import EnglishBoard, PegBoardConfigurationError, PegBoardMoveError, EnglishWinError
#NOTE: the from file must be the name Ian's file is saved as. I saved it as englishPeg.py on my computer.

##Function used to play trianlge peg (CAN ENG UP LOOKING LIKE THE FUNCTION TO PLAY ENGLISH PEG)
def playTPeg():
	raw_input("            O,4\n\n         O,3   1,3\n\n      O,2   1,2   2,2 \n\n   O,1   1,1   1,2   1,3\n\nO,O   1,0   2,0   3,0   4,0 \nMove: ")

#Function used to display the help screen when user selects help, requires the user to enter H from the start screen
def dispTHelp():
	helpInput = raw_input("\nThe game board is a triangle with 15 holes in the same shape as bowing pins,\nexcept with an extra row.\nThe game starts with pegs (golf tees) in all the holes except one;\nthe goal is to jump pegs one at a time,\nremoving the jumped peg until only one peg remains.\nUse the positions numbers listed below to move your pegs. Example:  8 to 6 would get rid of tee 7. \n      14 \n   12    13\n  9   1O   11 \n 5   6   7   8\nO  1   2   3   4  ")
	if helpInput == "S":
		dispEBoard()

#Function used for the user to actually play the english peg game
def playEPeg():
	board = EnglishBoard()
	print(board)
	while(True):
		try:
			engMove = raw_input("Move: ")
			sourceX, sourceY, targetX, targetY = [int(i) for i in engMove.split(',')]
			engMoveCoordS, engMoveCoordY = [sourceX,sourceY],[targetX,targetY]
			try:
				board.move(engMoveCoordS, engMoveCoordY)
				print(board)
			except PegBoardConfigurationError:
				print("Peg board configuration error, try again: ")
			except PegBoardMoveError:
				print("Move error, try again: ")
			except EnglishWinError:
				print("YOU've won! YAY!")
			except IndexError:
				print("You've entered coordinates outside the board, try again: ")
		except ValueError:
			print("Your input was incorrectly formatted, please try again: ")

#Function used to display the help screen for the english peg game
def dispEHelp():
	helpInput = raw_input("\nHelp for the Enlish Peg board game:\nThe objective of this game is to empty the board,\nleaving only one peg in the central square.\nTo begin enter S: ")
	if helpInput == "S":
		playEPeg()

#Menu that the user initially sees, depening on input will sectect the game and give an option to either start the game or get help about the game
menu = raw_input("|-----------------------------------|\n| To begin please enter:            |\n| 1 for English Peg                 |\n| 2 for Triangle Peg                |\n|-----------------------------------|\nGame choice: ")
if menu == "1":
	start = raw_input("\nEnter S to start or H for help:\n")
	if start == "S":
		playEPeg()
	if start == "H":
		dispEHelp()

if menu == "2":
	start2 = raw_input("Enter S to start or H for help: ")
	if start2 == "S":
		playTPeg()
	if start2 == "H":
		dispTHelp()
