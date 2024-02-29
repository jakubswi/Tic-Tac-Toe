def ask_player(player_num, board):
    while True:
        print(f"Player {player_num}")
        try:
            row = int(input("Which row do you choose (1-3):")) - 1
            col = int(input("Which column do you choose (1-3):")) - 1
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("This cell is already taken. Try again.")
            else:
                print("Invalid input. Row and column numbers must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def printing_matrix(matrix):
    print(f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}")
    print("----------")
    print(f" {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}")
    print("----------")
    print(f" {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}")

def check_for_win(matrix):
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != " ":
            return matrix[i][0]
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != " ":
            return matrix[0][i]
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":
        return matrix[0][2]
    return None

board= [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
printing_matrix(board)
current_player = "X"
while True:
    row, col = ask_player(1 if current_player == "X" else 2, board)
    board[row][col] = current_player
    printing_matrix(board)
    winner = check_for_win(board)
    if winner:
        print(f"Player {1 if winner == 'X' else 2} wins!")
        break
    elif all(cell != " " for row in board for cell in row):
        print("It's a draw!")
        break
    current_player = "O" if current_player == "X" else "X"
