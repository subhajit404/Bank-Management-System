import json
import random
import string
from pathlib import Path


class Bank:

    database = 'data.json'
    data  =[]
    try :
        if Path(database).exists():
            with open(database,'r') as file:
                data =json.loads(file.read)
        else:
            print("No such file exist")

    except Exception as err:
        print(err)

    @staticmethod
    def update():
        with open(Bank.database,'w') as file:
            file.write(json.dumps(Bank.data))


    def Create_Acc(self):
        info  = {
            "name" : input("Enter the name :-"),
            "age" : int(input("Enter the age :-")),
            "email" : input("Enter the Email :-"),
            "pin" :input("Enter the 4 no pin :-"),
            "accountno" : 1234,
            "balence" :0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4 :
            print("Sorry You can not create your account ")
        else:
            print("Your account create successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print(f"Please note your account no : {info['accountno']}")

            Bank.data.append(info)
            Bank.update()

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
print("Press 6 For Want to delete account ")



check = int(input("Enter Your response :-"))

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
