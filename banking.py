#we are creating bank aplication using oops class an their method and variables
import sys
class bank():
    bankname='NISHANT BANKING SERVICES'

    def __init__(self,name,cbal):
        print('welcome to Bank services')
        self.name=name
        self.bal=cbal
    def m1(self):
        print('your name:',self.name)
        print('your balance:',self.bal)
    def deposit(self):
        amt=int(input('enter an amount for deposit'))
        self.bal=self.bal+amt

        print('your current balance after deposition:',self.bal)
    def withdraw(self):
        print('enter an amount to withdraw')
        wd=int(input('enter amount in digit'))
        if wd > self.bal:
            print('insufficient balance...cannot perform further operations')

        elif wd < self.bal:
            wd=self.bal-wd
            print('your current balance after withdraw:', wd)
        else:
            print('sry..u have not entered any operations.. thankyou for banking')

print('welcome to',bank.bankname)
name=input('enter your name')
a1=bank(name,200)
a1.m1()
while True:

    print('Choose your Operation which you want to perform')
    print('D-deposit\nW-withdraw\nE-exit')
    z=input('enter your option')


    if z=='D':
        a1.deposit()
    elif z=='W':
        a1.withdraw()
    elif z=='E':
        print('thankyou for services')
        sys.exit()
    else:

        print('invalid option..please choose correct option')




