class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawl(self, amount):	# takes an argument that is the amount of the withdrawl
        self.account_balance -= amount
    def display_user_balance(self): # have this method print the user's name and account balance to the terminal
        self.display_balance = print(f"{self.name}, Your current balance is : {self.account_balance} Dollars") 
    def transfer_money(self, other_user, amount): # have this method decrease the user's balance by the amount and add that amount to other other_user's balance
        self.account_balance -= amount
        other_user.account_balance += amount
mitchell = User("Mitchell Golden", "aRealEmail@mail.com")
adrien = User("Adrien Dion", "LiteralRubixGod@mail.com")
anne = User("Anne Jurack", "Anneimations@mail.com")

mitchell.make_deposit(100)
mitchell.make_deposit(200)
mitchell.make_deposit(500)
mitchell.make_withdrawl(300)
mitchell.display_user_balance()
adrien.make_deposit(1000)
adrien.make_deposit(500)
adrien.make_withdrawl(500)
adrien.make_withdrawl(500)
adrien.display_user_balance()
anne.make_deposit(100000)
anne.make_withdrawl(1100)
anne.make_withdrawl(900)
anne.make_withdrawl(8000)
anne.display_user_balance()
mitchell.transfer_money(adrien, 502)
mitchell.display_user_balance()
adrien.display_user_balance()