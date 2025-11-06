
#银行账户*物价导向
class BankSystem:

    def __init__(account):
        account.accounts = {} #用class

    def create_account(account, name, initial_balance):
       #直接覆盖
       
       account.accounts[name] = initial_balance

    def deposit(account, name, amount):
        if name not in account.accounts:
            print("Account not found")
            return
        account.accounts[name] += amount


    def withdraw(account, name, amount):
        if name not in account.accounts:
            print("Account not found")
            return
        if amount > account.accounts[name]:   # 大于
            print("Insufficient funds")
            return
        account.accounts[name] -= amount

    def get_balance(account, name):
        if name not in account.accounts:
            print("Account not found")
            return
        print(account.accounts[name])

    def process_table(account, command_line): # use command is ??
        parts = command_line.strip().split() #用排队
        if not parts:
            return True

        action = parts[0]

        if action == "stop":
            return False 

        elif action == "create":
            name = parts[1]
            amount = int(parts[2])
            account.create_account(name, amount)

        elif action == "deposit":
            name = parts[1]
            amount = int(parts[2])
            account.deposit(name, amount)

        elif action == "withdraw":
            name = parts[1]
            amount = int(parts[2])
            account.withdraw(name, amount)

        elif action == "balance":
            name = parts[1]
            account.get_balance(name)

        else:
            pass

        return True  

#here mailn
if __name__ == "__main__":
    bank = BankSystem() #用class
    
    while True:
        try:
            theinput = input()
            if not bank.process_table(theinput):
                break


        except EOFError:
            break