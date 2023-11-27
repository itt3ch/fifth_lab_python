class BankAccount:
    def init(self, account_id, owner_name, balance=0.0):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into {self.owner_name}'s account. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.owner_name}'s account. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal.")

    def showAccount(self):
        print(f"Account ID: {self.account_id}, Owner: {self.owner_name}, Balance: ${self.balance}")

    def delete(self):
        print(f"Account {self.account_id} for {self.owner_name} is being deleted.")


class Bank:
    def init(self):
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def removeAccount(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                self.accounts.remove(account)
                print(f"Account {account_id} removed from the bank.")
                return
        print(f"Account {account_id} not found in the bank.")

    def sortAccountsByBalance(self):
        self.accounts.sort(key=lambda x: x.balance)

    def showAllAccounts(self):
        for account in self.accounts:
            account.showAccount()

    def delete(self):
        print("Bank is being deleted.")


def main():
    account1 = BankAccount(1, "John")
    account2 = BankAccount(2, "Jane")
    account3 = BankAccount(3, "Bob")

    bank = Bank()

    bank.addAccount(account1)
    bank.addAccount(account2)
    bank.addAccount(account3)

    account1.deposit(1000)
    account2.deposit(500)
    account3.deposit(1500.5)
    bank.sortAccountsByBalance()
    bank.showAllAccounts()

if name == "main":
    main()




