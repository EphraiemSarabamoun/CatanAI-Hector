from board import Board

board = Board()
board.generate_board()
print(board.hexes)
print(board.hexes[0].value, board.hexes[0].resource, board.hexes[0].edges)
print(board.edges)
print(board.edges[0].connections, board.edges[0].resources, board.edges[0].settlement)
