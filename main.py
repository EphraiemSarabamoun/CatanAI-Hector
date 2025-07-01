from board import Board
from display import Display

if __name__ == "__main__":
    board = Board()
    board.generate_board()
    
    display = Display(board)
    display.run()
