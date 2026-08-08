import json
import random
import string
from pathlib import Path


class Bank:
    def Create_Acc(self):
        pass
    def Deposite_Money(self):
        pass
    def Withdraw_Money(self):
        pass
    def Show_Details(self):
        pass
    def Update_Details(self):
        pass
    def Delete_Acc(self):
        pass

user = Bank()

print("Press 1 For create an account ")
print("Press 2 For Deposite money  ")
print("Press 3 For Withdraw Money ")
print("Press 4 For Want to show details  ")
print("Press 5 For Want to update  details  ")
print("Press 6 For Want to delete account  ")



check = int(input("Enter Your response "))

if check ==1:
    user.Create_Acc()
if check == 2:
    user.Delete_Acc()
if check == 3:
    user.Withdraw_Money()
if check ==4:
    user.Show_Details()
if check== 5 :
    user.Update_Details()
if check == 6 :
    user.Delete_Acc()
