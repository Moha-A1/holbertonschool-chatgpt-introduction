#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """
        Initializes the checkbook with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        CORRECTION: Le code original ne validait pas les montants positifs
        Avant: self.balance += amount  # Acceptait les montants négatifs
        Après: Validation des montants positifs avec message d'erreur
        
        Deposits a positive amount into the checkbook.

        Parameters:
        amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        CORRECTION: Le code original ne validait pas les montants positifs
        Avant: if amount > self.balance:  # Acceptait les montants négatifs
        Après: Validation complète des montants positifs et des fonds disponibles
        
        Withdraws a positive amount from the checkbook if sufficient funds are available.

        Parameters:
        amount (float): The amount to withdraw. Must be positive and <= current balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    CORRECTION: Le code original n'avait aucune gestion d'erreurs
    Avant: amount = float(input(...))  # Plantait avec ValueError si entrée non-numérique
    Après: Gestion complète des erreurs avec try/except et validation
    
    Main loop for user interaction with the checkbook.
    Supports deposit, withdraw, balance inquiry, and exit.
    Includes input validation and error handling.
    """
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action in ['deposit', 'withdraw']:
            try:
                amount_str = input("Enter the amount: $").strip()
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue

            if action == 'deposit':
                cb.deposit(amount)
            else:
                cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

# CORRECTION: Le code original plantait avec ValueError quand l'utilisateur entrait du texte
# Exemple d'erreur: ValueError: could not convert string to float: 'test'
# Maintenant le programme gère gracieusement toutes les entrées invalides
if __name__ == "__main__":
    main()
