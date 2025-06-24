def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_winner(board):
    # Rows, columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    # Tie check
    if all(cell != " " for row in board for cell in row):
        return "Tie"
    
    return None

def player_move(board):
    while True:
        try:
            move = input("Enter your move (row,col): ")
            row, col = map(int, move.split(","))
            if board[row][col] == " ":
                return row, col
            else:
                print("That spot’s already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Use format row,col (0-2).")

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe! You’re X. The AI is O.")

    while True:
        print_board(board)
        
        # Player Move
        row, col = player_move(board)
        board[row][col] = "X"
        if check_winner(board):
            break

        # AI Move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI has made its move.")
        if check_winner(board):
            break

    print_board(board)
    result = check_winner(board)
    if result == "Tie":
        print("It’s a tie!")
    else:
        print(f"{result} wins!")

# Run the game
if __name__ == "__main__":
    play_game()
