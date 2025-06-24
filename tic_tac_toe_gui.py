import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe: Sabryna vs AI")
root.geometry("400x450")

# Global game variables
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check winner
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    if all(cell != " " for row in board for cell in row):
        return "Tie"
    return None

# Minimax AI logic
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

def best_move():
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

# Handle player click
def player_move(row, col):
    if board[row][col] == " ":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")
        result = check_winner(board)
        if result:
            end_game(result)
            return
        ai_row, ai_col = best_move()
        if ai_row is not None:
            board[ai_row][ai_col] = "O"
            buttons[ai_row][ai_col].config(text="O", state="disabled")
            result = check_winner(board)
            if result:
                end_game(result)

# End game handler
def end_game(result):
    if result == "Tie":
        messagebox.showinfo("Game Over", "It's a tie!")
    else:
        messagebox.showinfo("Game Over", f"{result} wins!")
    restart_game()

# Restart button function
def restart_game():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")

# Create buttons grid
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Helvetica", 32), width=4, height=2,
                           command=lambda row=i, col=j: player_move(row, col))
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = button

# Restart button
restart_btn = tk.Button(root, text="Restart Game", font=("Helvetica", 14), command=restart_game)
restart_btn.grid(row=3, column=0, columnspan=3, pady=15)

# Run the app
root.mainloop()
