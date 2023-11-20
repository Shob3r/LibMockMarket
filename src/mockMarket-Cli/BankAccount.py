from clearScreen import clearScreen

class BankAccount:

    def __init__(self, initialDeposit, password = None):
        self.balance = float(initialDeposit)
        if password is None:
            self.setPassword()

    def setPassword(self):
        global password
        password = input('Please enter a password for your account: ')
        if password == '':
            print("Passwords cannot be empty!")
            clearScreen()
            self.setPassword()
        else:
            if password is not None:
                confirmPassword = input('Please input your password one more time to confirm it!')
                if password != confirmPassword:
                    print('Your passwords to not match ... ')
                    self.setPassword()
                else:
                    print('Password set! Your account is now ready!')
                    return
            else:
                print("Please enter a password!")
                self.setPassword()

    # Returns true if you have more balance than cost, false if you don't
    def canAfford(self, amount):
        if float(amount) <= self.balance:
            return True
        else:
            return False

    def makePurchase(self, amount):
        if self.checkPassword():
            if amount <= self.balance:
                self.balance -= amount
                print(f'{amount} spent from your account.')
                print(f'You now have ${self.balance} remaining.')
                return True
            else:
                print('You do not have enough funds left to afford this item.')
                return False
        else:
            return False

    def balanceReport(self):
        print(f'You have $ {self.balance} left in your account.')

    def checkPassword(self):
        passEntry = input('Please enter your password to confirm your identity: ')
        if passEntry == password:
            return True
        else:
            print('Incorrect password!')
            return False
