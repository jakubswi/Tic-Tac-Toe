# Tic Tac Toe Game

This is a simple implementation of the Tic Tac Toe game in Python.

## How to Play

1. Run the Python script.
2. Players take turns to choose a cell on the board to place their symbol.
3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
4. If all cells are filled and no player has won, the game ends in a draw.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the Python script.
4. Run the script using the command:
   ```
   python tictactoe.py
   ```

## Functionality

- `ask_player(player_num, board)`: Function to prompt the current player to choose a row and column for their move. Checks for valid input and whether the selected cell is already taken.
- `printing_matrix(matrix)`: Function to print the Tic Tac Toe board.
- `check_for_win(matrix)`: Function to check if a player has won the game. It checks for three consecutive symbols in rows, columns, and diagonals.
- The game is played in an infinite loop until a player wins or the game ends in a draw.

## License

This project is licensed under the [MIT License](LICENSE).

Enjoy playing Tic Tac Toe! 🎮
