#Welcome to PyBank
#Practice Project for Python OOP(Object oriented programming) and file handling
#This program uses a file named "bank.txt" to store data , the file is created itself
import random #for the generation of random numbers
import os #to check file existence 

accounts = [] #Empty list for storing accounts(objects)

class Account: #used for creating accounts
    def __init__(self , acc_no , name , acc_type , balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
        
if os.path.exists("bank.txt"): #Loads data from file to list
    with open("bank.txt") as file:
        for line in file:
            acc_no,name,acc_type,balance = line.strip().split(",")
            account = Account(int(acc_no),name,acc_type,int(balance))
            accounts.append(account)
else: #Creates file if it doesn't exist
    with open("bank.txt","w") as file:
        pass
            
print("-----------------------------------------")
print("           WELCOME TO PYBANK             ")
print("-----------------------------------------")

def menu(): #Menu module
    print()
    print("---------------------")
    print("         MENU        ")
    print("---------------------")
    print()
    print("1. CREATE A NEW ACCOUNT")
    print("2. VIEW ACCOUNT DETAILS")
    print("3. DEPOSIT MONEY")
    print("4. WITHDRAW MONEY")
    print("5. TRANSFER MONEY")
    print("6. SEARCH ACCOUNT")
    print("7. VIEW ALL ACCOUNTS")
    print("8. DELETE AN ACCOUNT")
    print("9. EXIT")
    print()

def func_save():#Saves data to file
    with open("bank.txt","w") as file:
        for account in accounts:
            file.write(f"{account.acc_no},{account.name},{account.acc_type},{account.balance}\n")
    
def func_create():#Create Account Module
    print()
    print("-------------------------------")
    print("       CREATE NEW ACCOUNT      ")
    print("-------------------------------")
    print()
    Name = input("Enter your name : ")
    while True:
        acc_no_id = random.randint(100000, 999999)
        is_unique = True  
        for account in accounts:
            if acc_no_id == account.acc_no:
                is_unique = False
                break
        if is_unique:
            acc_no = acc_no_id
            break  
    print("Choose the type of account you wish to create")
    print("1. Savings account")
    print("2. Current account")
    acc_type = None
    while acc_type == None:
        try:
            acc_type_id = int(input("Enter your choice : "))
        except ValueError:
            print("please enter a valid choice")
        else:
            if acc_type_id == 1:
                acc_type = "Savings account"
            elif acc_type_id == 2:
                acc_type = "Current account"
            else:
                print("Enter a choice from the above given options")
    j = 1 #Flag variable
    while j == 1:
        try:
            balance = int(input("Enter initial deposit amount : "))
        except ValueError:
            print("Enter amount appropriately")
        else:
            if balance < 0:
                print("amount can not be negative please enter appropriate amount")
            else:
                j=j+1
    account = Account(int(acc_no),Name,acc_type,int(balance))
    accounts.append(account)
    func_save()

def func_search():#Search Module
    print()
    print("-------------------------------")
    print("        SEARCH ACCOUNT         ")
    print("-------------------------------")
    print()
    Search_Found = False
    try:
        search_id = int(input("Enter Account Number of the account you wish to search : "))
    except ValueError:
        print("Please enter a valid Account Number")
    else:
        for account in accounts:
            if account.acc_no == search_id:
                Search_Found = True
                print("Account Found")
                print()
                print(f"Account Holder's Name : {account.name}")
                print(f"Account Number : {account.acc_no}")
                print(f"Account Type : {account.acc_type}")
                break
            else:
                Search_Found = False
        if Search_Found == False:
            print("Account Not Found , it does not exist")
            
def func_details():#View details module
    print()
    print("-------------------------------")
    print("     VIEW ACCOUNT DETAILS      ")
    print("-------------------------------")
    print()
    name_id = input("Enter Account Holder's Name whose account you wish to view : ")
    Search_Found = False
    try:
        search_id = int(input("Enter Account Number of the account whose details you want to see : "))
    except ValueError:
        print("Please enter a valid Account Number")
    else:
        for account in accounts:
            if account.acc_no == search_id and account.name == name_id:
                Search_Found = True
                print("Account Found")
                print()
                print(f"Account Holder's Name : {account.name}")
                print(f"Account Number : {account.acc_no}")
                print(f"Account Type : {account.acc_type}")
                print(f"Balance : {account.balance} ")
                break
            else:
                Search_Found = False
        if Search_Found == False:
            print("Account Not Found , it does not exist in the bank")
    
def func_deposit():#Deposit Module
    print()
    print("-------------------------------")
    print("         DEPOSIT MONEY         ")
    print("-------------------------------")
    print()
    Search_Found = False
    try:
        search_id = int(input("Enter Account Number of the Account you wish to deposit money into : "))
    except ValueError:
        print("Please enter a valid Account Number")
    else:
        for account in accounts:
            if account.acc_no == search_id:
                j = 1
                while j == 1:
                    try:
                        deposit = int(input("Enter amount that you wish to deposit : "))
                    except ValueError:
                        print("Enter amount appropriately")
                    else:
                        if deposit < 0:
                            print("amount can not be negative please enter appropriate amount")
                        else:
                            j=j+1
                account.balance = account.balance + deposit
                print("Balance Updated Successfully")
                Search_Found = True
                break
            else:
                Search_Found = False
        if Search_Found == False:
            print("Account Not Found , it does not exist")
    func_save()
    
def func_withdraw():#Withdraw Module
    print()
    print("-------------------------------")
    print("        WITHDRAW MONEY         ")
    print("-------------------------------")
    print()
    Search_Found = False
    try:
        search_id = int(input("Enter Account Number of the account you wish to withdraw money from : "))
    except ValueError:
        print("Please enter a valid Account Number")
    else:
        for account in accounts:
            if account.acc_no == search_id:
                j = 1
                while j == 1:
                    try:
                        withdraw = int(input("Enter amount that you wish to withdraw : "))
                    except ValueError:
                        print("Enter amount appropriately")
                    else:
                        if withdraw < 0:
                            print("amount can not be negative please enter appropriate amount")
                        elif withdraw > account.balance:
                            print(f"This Account does not have enough balance to withdraw {withdraw}")
                        else:
                            j=j+1
                account.balance = account.balance - withdraw
                print("Balance Updated Successfully")
                Search_Found = True
                break
            else:
                Search_Found = False
        if Search_Found == False:
            print("Account Not Found , it does not exist")
    func_save()

def func_transfer():#Transfer Module
    print()
    print("-------------------------------")
    print("         TRANSFER MONEY        ")
    print("-------------------------------")
    print()
    Search_Found = False
    try:
        search_id = int(input("Enter Sender's Account Number : "))
    except ValueError:
        print("Please enter a valid Account Number")
    else:
        for account in accounts:
            if account.acc_no == search_id:
                Search__Found = False
                try:
                    search__id = int(input("Enter Receiver's Account Number : "))
                except ValueError:
                    print("Please enter a valid Account Number")
                else:
                    for objects in accounts:
                        if search_id==search__id:
                            print("You can't send the money to the same account from which you send")
                        elif objects.acc_no == search__id:
                            j = 1
                            while j == 1:
                                try:
                                    exchange = int(input("Enter amount that you wish to send : "))
                                except ValueError:
                                    print("Enter amount appropriately")
                                else:
                                    if exchange<0:
                                        print("amount can not be negative please enter appropriate amount")
                                    elif exchange > account.balance:
                                        print(f"This Account does not have enough balance to send {exchange}")
                                    else:
                                        j=j+1
                            account.balance = account.balance - exchange
                            objects.balance = objects.balance + exchange
                            print("Money Transferred Successfully")
                            Search__Found = True
                            break
                        else:
                            Search__Found = False
                    if Search__Found == False:
                        print("Account Not Found , it does not exist")
                Search_Found = True
                break
            else:
                Search_Found = False
        if Search_Found == False:
            print("Account Not Found , it does not exist")
    func_save()

def func_view_all(): #View all Module
    print()
    print("-------------------------------")
    print("         ALL ACCOUNTS          ")
    print("-------------------------------")
    print()
    for account in accounts:
        print()
        print(f"Account Holder's Name : {account.name}")
        print(f"Account Number : {account.acc_no}")
        print(f"Account Type : {account.acc_type}")
        print()
        
def func_delete(): #Delete Module
    print()
    print("-------------------------------")
    print("         DELETE ACCOUNT        ")
    print("-------------------------------")
    print()
    Search_Found = False
    try:
        delete_id = int(input("Enter Account number that you wish to delete : "))
    except ValueError:
        print("Please enter a valid Account Number")
    else:
        for account in accounts:
            if account.acc_no == delete_id:
                Search_Found = True
                print("Account Found")
                print()
                print(f"Account Holder's Name : {account.name}")
                print(f"Account Number : {account.acc_no}")
                print(f"Account Type : {account.acc_type}")
                print()
                print("Are you sure you want to delete this account ?")
                print("1. Yes")
                print("2. No")
                choice_id = None
                while choice_id == None:
                    try:
                        choice_id = int(input("Enter your choice : "))
                    except ValueError:
                        print("please enter a valid choice")
                    else:
                        if choice_id == 1:
                            accounts.remove(account)
                            print("Account Deleted Successfully")
                        elif choice_id == 2:
                            print("Account Deletion Cancelled")
                        else:
                            print("Enter a choice from the above given options")
                            choice_id = None
                break
            else:
                Search_Found = False
        if Search_Found == False:
            print("Account Not Found , it does not exist")
    func_save()

while True: #Feature Selection
    menu()
    try: 
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Enter a Valid Choice")
    else:
        if choice == 1:
            func_create()
        elif choice == 2:
            func_details()
        elif choice == 3:
            func_deposit()
        elif choice == 4:
            func_withdraw()
        elif choice == 5:
            func_transfer()
        elif choice == 6:
            func_search()
        elif choice == 7:
            func_view_all()
        elif choice == 8:
            func_delete()
        elif choice == 9:
            print()
            print("----------------------------")
            print(" THANK YOU FOR USING PYBANK ")
            print("----------------------------")
            break
        else:
            print()
            print("Enter a valid choice from above given options")
            print()
