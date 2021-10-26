class Atm:
    def __init__(self,cardNo,pin):
        self.cardNo=cardNo
        self.pin=pin

    def checkBalance(self):
        print("Your balance account has 50000")

    def withdrawal(self,amount):
        newAmount=50000-amount
        print("You have withdrawn amount "+str(amount)+" your remaining amout is "+str(newAmount))

cardNo=input("Enter your cardNo")
pin=input("Enter your pin no")
user=Atm(cardNo,pin)
print("Choose your activity")
print("1.BalanceEnquiry 2.Withdrawal")
choice=int(input("Enter Your choice"))
if choice==1:
    user.checkBalance()
elif choice==2:
    amount=int(input('Enter amount u want to withdraw'))
    user.withdrawal(amount)
else:
    print("Enter a valid number")