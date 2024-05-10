def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Augmentation de la longueur pour mieux s'aligner

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    count = 0  # Compteur pour vérifier l'égalité
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " ":
                board[row][col] = player
                count += 1  # Incrémentation du compteur à chaque coup valide
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid row and column.")

        if count == 9:  # Si le tableau est rempli sans gagnant
            print_board(board)
            print("It's a tie!")
            return

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
