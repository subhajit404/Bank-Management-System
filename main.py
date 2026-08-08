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
                data =json.loads(file.read())
        else:
            print("No such file exist")

    except Exception as err:
        print(err)

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as file:
            file.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def Create_Acc(self):
        info  = {
            "name" : input("Enter the name :-"),
            "age" : int(input("Enter the age :-")),
            "email" : input("Enter the Email :-"),
            "pin" :input("Enter the 4 no pin :-"),
            "accountNo." : Bank.__accountgenerate(),
            "balance" :0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4 :
            print("Sorry You can not create your account ")
        else:
            print("Your account create successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note your account no ")

            Bank.data.append(info)
            Bank.__update()

    def Deposite_Money(self):
        acc_no = input("Please Tell us your account no : ")
        pin = int(input("Enter your pin :"))
        userdata = [i for i in Bank.data if i['accountNo.'] == acc_no and i['pin']==pin]
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("Enter the amount you want to deposit :-"))
            if amount >10000 or amount < 0 :
                print("We accept amount only between 1 to 10000 ")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount Depositrd Successfully")
                

    def Withdraw_Money(self):
        acc_no = input("Please Tell us your account no : ")
        pin = int(input("Enter your pin :"))
        userdata = [i for i in Bank.data if i['accountNo.'] == acc_no and i['pin']==pin]
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("Enter the amount you want to Withdraw :-"))
            if amount>userdata[0]['balance'] :
                print("Insufficent balence")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount Withdraw Successfully")


    def Show_Details(self):
        acc_no = input("Please Tell us your account no : ")
        pin = int(input("Enter your pin :"))
        userdata = [i for i in Bank.data if i['accountNo.'] == acc_no and i['pin']==pin]
        if userdata == False:
            print("Sorry no data found")
        else:
            print("Your information are :-")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def Update_Details(self):
        acc_no = input("Please Tell us your account no : ")
        pin = int(input("Enter your pin :"))
        userdata = [i for i in Bank.data if i['accountNo.'] == acc_no and i['pin']==pin]
        if userdata == False:
            print("Sorry no data found")
        else:
            print("You can not change age , accountNo. , balance")

            print("Fill the details for change or liv it emty if no change ")

            newdata = {
                'name': input("enter the name or liv it if you dont want to change name :-"),
                'email': input("Enter new email or enter :-"),
                'pin':int(input("Enter new pin or enter :-"))
            }

            if newdata['name'] =="":
                newdata['name'] = userdata[0]['name']
            if newdata['email'] =="":
                newdata['email'] = userdata[0]['email']
            if newdata['pin'] =="":
                newdata['pin'] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i]= newdata[i]
            Bank.__update()
            print("Update details successfully")

            



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
    user.Deposite_Money()
if check == 3:
    user.Withdraw_Money()
if check ==4:
    user.Show_Details()
if check== 5 :
    user.Update_Details()
if check == 6 :
    user.Delete_Acc()
