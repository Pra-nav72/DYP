def Balance(balance):
    b = balance
    return b

def deposit(balance):
    print("******************************")
    amount = float(input("Enter the deposit amount: "))
    print("******************************")
    if amount<0:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Amount Can't be negative!")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^")
        return balance
    else:
        balance += amount
        print("**********************************************")
        print(f"your amount ₹{amount} is deposited!")
        print("**********************************************")

        return balance


def withdraw(balance):  

    print("******************************")
    amount = float(input("Enter the withdrawal amount: "))
    print("******************************")

    if amount>balance:
        print("^^^^^^^^^^^^^^^^^^^^")
        print("Insuffiecient funds!")
        print("^^^^^^^^^^^^^^^^^^^^")
        return balance
    else:
        balance -= amount
        
        print("************************************")
        print(f"your amount ₹{amount} is withdrawn!")
        print("************************************")
        return balance

balance = 0
is_running=True

while is_running:

    print('---------------------------------')
    print("         Bank System        ")
    print("---------------------------------")
    print("1. Check Balance\n2. Deposit\n3.Withdraw \n4.Exit")
    print("#################################")

    inp = input("Enter the value(1-4): ")

   
    if inp=='4':
        is_running=False
        break

    elif inp=='1':
       b= Balance(balance)

       print("**************************")
       print(f"your balance is ₹{b:.2f}")
       print("**************************")

    elif inp =='2':
        balance=deposit(balance)
       
    elif inp=='3':
       balance= withdraw(balance)

    else:
        print("*************************")
        print("Invalid Input! Try Again!")    
        print("*************************")
    