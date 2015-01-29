
import PegSolitaire

def main():
    source = [2,4]
    target = [4,4]
    board = PegSolitaire.EnglishBoard()
    board.move(source, target)
    print(board.board)
    
          
          
          
main()