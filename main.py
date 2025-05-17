import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return cell
    print("-------------")
    for row in board:
        print("|", " | ".join(colored(cell) for cell in row), "|")
        print("-------------")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number from 1 to 9.")

def ai_move(board):
    available = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['X', 'O']]
    if available:
        row, col = random.choice(available)
        board[row][col] = 'O'

def play_game():
    board = [['1','2','3'],['4','5','6'],['7','8','9']]
    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        player_move(board)
        display_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_move(board)
        display_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()
