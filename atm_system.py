balance = 1000

while True:
    print("\n---ATM MENU---")
    print("1 . Check Balance ")
    print("2 . Deposite ")
    print("3 . Withdraw ")
    print("4 . Exit ")

    choice = input("Enter your choice 1-4 : ")

    if choice == "1":
        print("Your current balance is: ",balance)
    elif choice == "2":
        Amount = int(input("Enter the amount :"))
        balance += Amount
        print("Deposite successfull..")
    elif choice == "3":
        amount =int(input("Enter the withdraw amount :"))
        
        if amount <= balance:
            balance -= amount 
            print("please collect your cash ")
        else:
            print("Insufficent balance ") 
    elif choice == "4":
        print("Thank you for Using this ATM. See you again BYE !!")
        break
    else:
        print("Invalide choice . Please try again ")