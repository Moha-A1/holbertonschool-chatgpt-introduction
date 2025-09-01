#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.won = False

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        
        if self.revealed[y][x]:
            return True
        
        # Vérifier si c'est une mine
        if (y * self.width + x) in self.mines:
            return False
        
        # Révéler la cellule
        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and 0 <= ny < self.height and 
                        not self.revealed[ny][nx] and 
                        (ny * self.width + nx) not in self.mines):
                        self.reveal(nx, ny)
        
        return True

    def check_win(self):
        """
        CORRECTION: Cette fonction était complètement manquante dans le code original
        Elle est essentielle pour détecter quand le joueur a gagné
        """
        # Vérifie si le joueur a gagné en révélant toutes les cellules non-mines
        total_cells = self.width * self.height
        revealed_cells = sum(sum(row) for row in self.revealed)
        return revealed_cells == (total_cells - len(self.mines))

    def play(self):
        while not self.game_over and not self.won:
            self.print_board()
            
            if self.check_win():
                self.won = True
                break
            
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                if not self.reveal(x, y):
                    self.game_over = True
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except KeyboardInterrupt:
                print("\nGame interrupted.")
                break
        
        if self.won:
            self.print_board(reveal=True)
            print("Congratulations! You've won the game.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
