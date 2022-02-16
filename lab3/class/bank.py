class bank():# class bank
    def __init__(self,owner,balance):
        self.balance = balance
        self.owner = owner

    def deposit(self,money):#method to deposit money
        self.balance += money
        print(f'{self.owner}, succesfully added {money},your balance now is {self.balance}')
        return self.balance

    def withdraw (self,withd):#method to withdraw money
        if withd > self.balance:#prevents the overdrawn
            print(f'{self.owner}, you, need {withd-self.balance} to withdraw from bank account')
        else:#succesfully widthdrawn
            print(f'{self.owner}, you, succesfully withdrawed {withd}, your balance now is {self.balance-withd}')

owner = input('Who is activating?\n')
balance = int(input())
action = input('\nWhat do you want to do?\n')
f = bank(owner,balance)

while(action != 'stop'):
    if(action == 'deposit'):
        money = int(input("\nHow much money do you want to add?\n"))
        f.deposit(money)
    elif(action == 'withdraw'):
        withd = int(input('\nHow much money do you want to withdraw?\n'))
        f.withdraw(withd)
    elif(action == 'stop'):
        break
    else:
        print('Unknown command, try again') 
    action = input('\nWhat do you want to do?\n')