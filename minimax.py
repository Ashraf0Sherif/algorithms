def minimax(state, depth, is_maximizing_player, evaluate_fn, get_moves_fn, make_move_fn, undo_move_fn, game_over_fn):
    if depth == 0 or game_over_fn(state):
        return evaluate_fn(state), None
    
    possible_moves = get_moves_fn(state)
    
    if is_maximizing_player:
        best_score = float('-inf')
        best_move = None
        
        for move in possible_moves:
            make_move_fn(state, move)
            
            score, _ = minimax(state, depth - 1, False, evaluate_fn, get_moves_fn, make_move_fn, undo_move_fn, game_over_fn)
            
            undo_move_fn(state, move)
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        
        for move in possible_moves:
            make_move_fn(state, move)
            
            score, _ = minimax(state, depth - 1, True, evaluate_fn, get_moves_fn, make_move_fn, undo_move_fn, game_over_fn)
            
            undo_move_fn(state, move)
            
            if score < best_score:
                best_score = score
                best_move = move
        
        return best_score, best_move

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def is_game_over(self):
        return self.get_winner() != None or all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def get_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
        
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != ' ':
                return self.board[0][j]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def make_move(self, move):
        i, j = move
        self.board[i][j] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def undo_move(self, move):
        i, j = move
        self.board[i][j] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def evaluate(self):
        winner = self.get_winner()
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        else:
            return 0

if __name__ == "__main__":
    game = TicTacToe()
    
    def evaluate_fn(state):
        return state.evaluate()
    
    def get_moves_fn(state):
        return state.get_possible_moves()
    
    def make_move_fn(state, move):
        state.make_move(move)
    
    def undo_move_fn(state, move):
        state.undo_move(move)
    
    def game_over_fn(state):
        return state.is_game_over()
    
    print("Initial board:")
    game.print_board()
    
    while not game.is_game_over():
        if game.current_player == 'X':
            print("\nYour turn (X)")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            move = (row, col)
        else:
            print("\nAI's turn (O)")
            _, move = minimax(game, 5, False, evaluate_fn, get_moves_fn, make_move_fn, undo_move_fn, game_over_fn)
            print(f"AI chooses: {move}")
        
        game.make_move(move)
        game.print_board()
    
    winner = game.get_winner()
    if winner:
        print(f"\nWinner: Player {winner}")
    else:
        print("\nGame ended in a draw")