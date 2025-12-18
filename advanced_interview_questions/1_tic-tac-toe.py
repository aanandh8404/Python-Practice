# # Tic Tac Toe Game

# def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)
#     print()


# def check_winner(board, player):
#     # Check rows
#     for row in board:
#         if all(cell == player for cell in row):
#             return True

#     # Check columns
#     for c in range(3):
#         if all(board[r][c] == player for r in range(3)):
#             return True

#     # Check diagonals
#     if (board[0][0] == board[1][1] == board[2][2] == player) or \
#        (board[0][2] == board[1][1] == board[2][0] == player):
#         return True

#     return False


# def is_draw(board):
#     return all(board[r][c] != " " for r in range(3))


# def tic_tac_toe():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"

#     while True:
#         print_board(board)
#         print(f"Player {current_player}, enter your move (row and column 1-3):")

#         try:
#             r, c = map(int, input().split())
#             r -= 1
#             c -= 1

#             if r not in range(3) or c not in range(3):
#                 print("Invalid position! Try again.\n")
#                 continue

#             if board[r][c] != " ":
#                 print("Cell already taken! Try another.\n")
#                 continue

#         except ValueError:
#             print("Please enter two numbers separated by space.\n")
#             continue

#         # Place the move
#         board[r][c] = current_player

#         # Check winner
#         if check_winner(board, current_player):
#             print_board(board)
#             print(f"🎉 Player {current_player} wins!")
#             break

#         # Check draw
#         if is_draw(board):
#             print_board(board)
#             print("It's a draw!")
#             break

#         # Switch player
#         current_player = "O" if current_player == "X" else "X"


# # Run the game
# tic_tac_toe()

# Simple Tic Tac Toe

board = [" "]*9
current = "X"

def show():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

for i in range(9):
    show()
    pos = int(input(f"Player {current}, choose (1-9): ")) - 1

    if board[pos] != " ":
        print("Invalid move!")
        break

    board[pos] = current

    if check(current):
        show()
        print(f"🎉 Player {current} wins!")
        break

    current = "O" if current == "X" else "X"
else:
    show()
    print("It's a draw!")
