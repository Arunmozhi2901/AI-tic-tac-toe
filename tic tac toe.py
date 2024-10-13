import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'  # X starts
        self.buttons = [tk.Button(master, text=' ', font='Arial 20', width=5, height=2,
                                   command=lambda i=i: self.player_move(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def player_move(self, index):
        if self.board[index] == ' ' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X')
            if not self.check_winner('X'):
                self.current_player = 'O'
                self.ai_move()

    def ai_move(self):
        index = self.best_move()
        if index is not None:
            self.board[index] = 'O'
            self.buttons[index].config(text='O')
            if not self.check_winner('O'):
                self.current_player = 'X'

    def best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'  # Simulate AI move
                score = self.minimax(self.board, False)  # Minimize for the opponent
                self.board[i] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def minimax(self, board, is_maximizing):
        if self.check_winner_helper(board, 'O'):
            return 1  # AI wins
        elif self.check_winner_helper(board, 'X'):
            return -1  # Player wins
        elif ' ' not in board:
            return 0  # Draw

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'  # Simulate AI move
                    score = self.minimax(board, False)  # Minimize for the opponent
                    board[i] = ' '  # Undo move
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'  # Simulate player move
                    score = self.minimax(board, True)  # Maximize for the AI
                    board[i] = ' '  # Undo move
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        if self.check_winner_helper(self.board, player):
            self.display_winner(player)
            return True
        if ' ' not in self.board:
            self.display_draw()
            return True
        return False

    def check_winner_helper(self, board, player):
        for i in range(3):
            if board[i*3] == board[i*3 + 1] == board[i*3 + 2] == player:
                return True
            if board[i] == board[i + 3] == board[i + 6] == player:
                return True
        if board[0] == board[4] == board[8] == player or \
           board[2] == board[4] == board[6] == player:
            return True
        return False

    def display_winner(self, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        self.reset_game()

    def display_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
