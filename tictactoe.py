import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#f0f0f0")  # Light background
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.style = ttk.Style()
        self.setup_styles()
        self.create_board()

    def setup_styles(self):
        """Configure custom styles for buttons."""
        self.style.configure("TButton", font=("Arial", 24), padding=5)
        self.style.map("TButton",
                       foreground=[('active', 'black')],
                       background=[('active', '#d6d6d6')],
                       relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

    def create_board(self):
        """Create the 3x3 board with styled buttons."""
        for row in range(3):
            for col in range(3):
                button = ttk.Button(
                    self.root, text="", style="TButton",
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")
                self.root.grid_rowconfigure(row, weight=1)
                self.root.grid_columnconfigure(col, weight=1)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        """Handle a player's move."""
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            button["style"] = "Player.X.TButton" if self.current_player == "X" else "Player.O.TButton"
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        """Check if the current player has won."""
        # Check the row
        if all(self.buttons[row][c]["text"] == self.current_player for c in range(3)):
            return True
        # Check the column
        if all(self.buttons[r][col]["text"] == self.current_player for r in range(3)):
            return True
        # Check the diagonal
        if row == col and all(self.buttons[i][i]["text"] == self.current_player for i in range(3)):
            return True
        # Check the anti-diagonal
        if row + col == 2 and all(self.buttons[i][2-i]["text"] == self.current_player for i in range(3)):
            return True
        return False

    def is_draw(self):
        """Check if the game is a draw."""
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        """Reset the board for a new game."""
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button["text"] = ""
                button["style"] = "TButton"
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)

    # Additional styles for players
    game.style.configure("Player.X.TButton", foreground="blue", background="#add8e6")
    game.style.configure("Player.O.TButton", foreground="red", background="#f08080")

    root.mainloop()

