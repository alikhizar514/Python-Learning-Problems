


class BankAccount:
    def __init__(currentAccount_object, accNumber, name, balance):
        currentAccount_object.accNumber = accNumber
        currentAccount_object.name = name
        currentAccount_object.balance = balance
    def Deposit(currentAccount_object, amount):
        currentAccount_object.balance += amount
        print("Money deposited successfully, your current balance is ",currentAccount_object.balance)
    def Withdrawl(currentAccount_object, amount):
        if(currentAccount_object.balance >= amount):
            currentAccount_object.balance -= amount
            print("Money withdrawed successfully, your current balance is ",currentAccount_object.balance)
        else:
            print("You have not enough balance to withdraw ",currentAccount_object.balance)    
    def bankfees(currentAccount_object):
        fees = currentAccount_object.balance * 0.05
        currentAccount_object.balance -=fees
        print("Fee submitted successfully, your current balance is ",currentAccount_object.balance)
    def display(currentAccount_object):
        print(currentAccount_object.name,"'s details : ")
        print("Account Number : ",currentAccount_object.accNumber)
        print("Balance : ", currentAccount_object.balance)

account = BankAccount(999999999999,"Ali Khizar",10000)
account.Deposit(500)
account.Withdrawl(250)
account.bankfees()
account.display()