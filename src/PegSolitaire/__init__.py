''''Authors: Ian Foertsch, Tyler Fitzgerald, Kaila Gervais, Michael Fritz
Date: 1/22/15
Project: Peg Solitaire
Class: CS 205
'''




PEG = 1
OPEN = 0
NOSPACE = 9
STARTROW = 4
STARTCOLUMN = 4
BOARDSIZE = 9
TWOSPACES = 2

'''The PegBoard superclass contains the coordinate checking logic which ensures that the move is legal.
This logic is largely shared between triangle solitaire and english solitaire, with the exception that 
triangle solitaire has an extra diagonal degree of movement.'''
class PegBoard:
    
    '''The check coordinate bounds method returns false if the source or target coordinates are outside 
    of the bounds of the lists representing the board '''
    def checkCoordinateBounds(self, source, target):
        
        #For the length of the source coordinates
        for index in range(len(source)):
            #Bundle the source and target into a single tuple in order to promote code reuse below
            for coordinates in (source, target):
                #if any value in the array is greater than or equal to the board size, or less than 
                #zero, return false.
                if coordinates[index] >= BOARDSIZE or coordinates[index] < 0:
                    return False
        #If all error checks are good, return true, indicating that the given coordinates are inside the
        #bounds of the game board lists.
        return True
    
    '''The check source and target method checks to ensure that the source space on the board is occupied by a peg, 
    and that the target space on the board is open, returning false if either condition is violated.'''
    def checkSourceAndTarget(self, source, target):
        if(self.board[source[0]][source[1]] != PEG):
            return False
        elif(self.board[target[0]][target[1]] != OPEN):
            return False
        else:
            return True
          
        
    '''CheckLegalMoveEnglish method checks the source and target coordinates to ensure the moves are orthogonal,
    as well as checking to see if the source and target are exactly two spaces away from each other.'''
    def checkLegalMoveEnglish(self, source, target):
        
        for index in range(len(source)):
            #if the source and the target match for a given index, then this is the row or column in which they are aligned
            if source[index] == target[index]:
                if index + 1 >= len(source):     
                    return abs(source[0] - target[0]) == TWOSPACES
                else:
                    return abs(source[index+1]-target[index+1]) == TWOSPACES
        
        return False
                   
    
    '''Check Peg Between examines the space between the source and the target coordinates to ensure
    that there is a peg present between the two coordinates.'''
    def checkPegBetween(self, source, target):
        
        spaceBetween = self.indexOfPegBetween(source, target)
        
        return self.board[spaceBetween[0]][spaceBetween[1]] == PEG
                    
    
    '''Index of peg Between contains the logic which returns the index coordinates of the space between the target'''        
    def indexOfPegBetween(self, source, target):
        
        #set to open contains the coordinates of the space on the board which we wish to set to "open"
        pegBetweenCoordinates = []
        #row delta is the absolute change in the row coordinate for the "Peg Between"
        for i in range(len(source)):     
            #round statement added to the append to ensure that the calling function receives 
            #integers rather than floats
            pegBetweenCoordinates.append(round(source[i] - (source[i]-target[i])/2))
        
        
        return pegBetweenCoordinates
            
'''NOTE: PUT ALL EXCEPTION DEFINITIONS HERE'''
class PegBoardConfigurationError(Exception):
    '''Raise this exception when there is some pertinent error in the 
    gameboard which prevents a specified move'''
class PegBoardMoveError(Exception):
    '''Raise this exception when the specified move is not 
    legal according to the specified pegboard move rules'''
        
    
class EnglishBoard(PegBoard):

    def __init__(self):
        
        self.board = [[1 for x in range(BOARDSIZE)] for x in range(BOARDSIZE)]
    
        for row in range(BOARDSIZE):
            for column in range(BOARDSIZE):
                if row < 3 and column < 3:
                    self.board[row][column] = NOSPACE
                elif row > 5 and column < 3:
                    self.board[row][column] = NOSPACE
                elif row < 3 and column >5:
                    self.board[row][column] = NOSPACE
                elif row > 5 and column > 5:
                    self.board[row][column] = NOSPACE
                elif row == STARTROW and column == STARTCOLUMN:
                    self.board[row][column] = OPEN
                else:
                    self.board[row][column] = PEG
                    
        
    '''The Move method accepts a pair of two-integer lists describing the coordinates of the source 
    space and target space of the move. The method first checks to see if the specified move is legal. 
    If it is not legal, a variety of exceptions are 
    thrown. If the move passes all the specified tests, then it is accepted and updated on the board.'''
    def move(self, source, target):
        #Check the exception-raising issues. 
        #1.) Firstly, whether the specified coordinates are within the index boundaries of the pertinent lists.
        if(not(self.checkCoordinateBounds(source, target))):
            raise IndexError("Specified Coordinates Outside of Game Boundaries.")
        #2.) Check the Source and target to ensure that the source space is occupied by a peg, and that the target space is open
        elif(not(self.checkSourceAndTarget(source, target))):
            raise PegBoardConfigurationError("Source coordinate is not occupied by a peg, or the target space is not open.")
        #3.) check that the move is legal according to the specified move rules contained in the checkLegalMove method
        elif(not(self.checkLegalMoveEnglish(source, target))):
            raise PegBoardMoveError("Specified move is not orthogonal, or the move is greater or less than 2 spaces.")
        #4.) check that the specified source and target space have a space occupied by a peg between them.
        elif(not(self.checkPegBetween(source, target))):
            raise PegBoardMoveError("Specified move does not contain a peg between the source and target space.")
        
        
        ####IF AND ONLY IF ALL ERROR CHECKS ARE PASSED
        # Execute the move on the board, setting the source coordinate to OPEN, and the target coordinate to PEG.
        self.board[source[0]][source[1]] = OPEN
        self.board[target[0]][target[1]] = PEG
        #lastly, get the index of the intervening peg and set it to open(removing the peg)
        pegBetween = self.indexOfPegBetween(source, target)
        self.board[pegBetween[0]][pegBetween[1]] = OPEN
        