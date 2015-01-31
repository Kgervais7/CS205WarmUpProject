'''Author: Ian Foertsch
Project: English Peg Solitaire
Date: 1/31/15'''
from PegSolitaire import EnglishBoard, PegBoardConfigurationError, PegBoardMoveError, \
    EnglishWinError

'''PegMain contains an example board game loop and necessary try/except statements
required to catch all the possible board exceptions and data entry errors'''
def main():
    board = EnglishBoard()
    print(board)
    while(True):
        
        try: 
            move = input("Enter move as sourcex,sourcey,targetx,targety:")
            sourcex, sourcey, targetx, targety = [int(i) for i in move.split(',')]
            source, target = [sourcex,sourcey],[targetx,targety]
            try:
                board.move(source, target)
                print(board)
            except PegBoardConfigurationError:
                print("PegBoardConfiguration Error: Either a peg is not at the source " +\
                      "or the target is occupied by a peg.")
            except PegBoardMoveError:
                print("Move Error: the specified move is not legal according to the rules" +\
                      " of English Peg Solitaire: The move must be orthogonal, and jump over exactly one space.")
            except EnglishWinError:
                print("Congratulations: You've Won!")
            except IndexError:
                print("IndexError: You've entered coordinates outside the boundaries of the board.")
        except ValueError:
            print("Your input was incorrectly formatted, please try again.")
           
           
main()