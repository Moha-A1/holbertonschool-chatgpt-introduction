#!/usr/bin/python3
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """
    Displays the current state of the board with column/row indices and aligned grid.
    """
    clear_screen()
    print("\n    1   2   3")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        row_str = " | ".join(f"{cell:^1}" for cell in row)
        print(f"{i + 1} | {row_str} |")
        print("  +---+---+---+")
    print("\n")

def check_winner(board):
    """
    CORRECTION: Le code original retournait True/False au lieu du joueur gagnant
    Avant: return True  # Ne disait pas qui avait gagné
    Après: return row[0]  # Retourne le joueur gagnant ("X" ou "O")
    
    Checks if there is a winner on the board.

    Return:
    str: "X" or "O" if there's a winner ; none otherwise
    """
    # CORRECTION: Retour du joueur gagnant au lieu de True/False
    # Rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]  # Retourne "X" ou "O" au lieu de True
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]  # Retourne le joueur gagnant
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Retourne le joueur gagnant
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Retourne le joueur gagnant
    return None

def is_board_full(board):
    """
    CORRECTION: Cette fonction était complètement manquante dans le code original
    Le code original ne gérait pas les matchs nuls (égalités)
    
    Return: true if the board is full (i.e., no empty cells)
    """
    # CORRECTION: Ajout de la détection des matchs nuls
    # Le code original ne vérifiait jamais si le plateau était plein
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    CORRECTION: Le code original avait plusieurs erreurs critiques
    1. Pas de gestion d'erreurs pour les entrées non-numériques
    2. Pas de validation des coordonnées
    3. Pas de gestion des matchs nuls
    4. Message de victoire incorrect (mauvais joueur)
    
    Main loop to play a game of Tic Tac Toe.
    Handles user input, game state updates, and error management.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            col = int(input(f"Enter Column for player {player}: ")) - 1
            row = int(input(f"Enter Row for player {player}: ")) - 1
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid coordinates. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        except EOFError:
            print("\nInput interrupted. Exiting game.")
            return

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

# CORRECTION: Le code original avait plusieurs erreurs critiques
# 1. ValueError si entrée non-numérique (ex: "abc" au lieu de coordonnées)
# 2. Pas de validation des coordonnées (ex: entrer 5 au lieu de 0-2)
# 3. Pas de gestion des matchs nuls
# 4. Message de victoire incorrect (affichait le mauvais joueur)
# Maintenant le jeu gère toutes ces situations gracieusement
if __name__ == "__main__":
    tic_tac_toe()
