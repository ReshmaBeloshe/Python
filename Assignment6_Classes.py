# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:47:53 2018

@author: reshmb
"""
#1.	Write a class to implement a television in Python (Hint: Properties: state, channel, volume. Methods: changing the channel, volume increase, volume decrease, Switch ON/OFF)

class TeleVision:
    def __init__(self):
        self.state = True
        self.channel = 5
        self.volume = 1
        
    def changeChannel(self):
        self.channel = int(input("Please enter new channel numner"))
        if (self.channel > 500):
            self.channel  =  self.channel
        
    def changeStatus(self):
        if (self.state == True):
            self.state = False
        else:
            self.state = True
            
    def increaseVolume(self):
        if (self.volume < 10):
            self.volume += 1

    def decreaseVolume(self):
        if (self.volume > 0):
            self.volume -= 1

    
TV1 = TeleVision()

TV1.changeChannel()
TV1.channel

TV1.changeStatus()
TV1.state

TV1.increaseVolume()
TV1.volume

TV1.decreaseVolume()
TV1.volume

#2.Write a class to implement a Bank Account in Python (Hint: Properties: account no., account holder’s name, current balance. Methods: deposit, withdraw)

class BankAccount:
    def __init__(self):
        self.accNumber = int(input("Please enter unique account number"))
        self.name = input("Please enter account holder's name")
        self.balance = int(input("Please enter initial balance in account"))
        
    def withdraw(self):
        withdraw_amt = int(input("Please enter the amount to withdraw"))
        if (self.balance > 1000):
            self.balance  -=  withdraw_amt

    def deposit(self):
        deposit_amt = int(input("Please enter the amount to withdraw"))
        self.balance  +=  deposit_amt

account1 = BankAccount()
 
account1.withdraw()
account1.balance
      
account1.deposit()
account1.balance