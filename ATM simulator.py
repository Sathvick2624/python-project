balance=90000
correct_pin=1234
print("Welcome to Python ATM ")
attempt=0
logged_in=False
while attempt<3:
    user_pin=int(input("Enter your 4 digit pin:"))
    

    if user_pin!=correct_pin:
        attempt+=1
        print("incorrect pin\nenter correct pin")
        print("attempts left",3-attempt)
        if attempt==3:
            print("Account blocked")
            print("You have reached maximum attempts")
            break
    else:
        print("Login successfull")
        logged_in=True
        break
if logged_in:
    while True:
        print("\n=====ATM MENU======")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Change Pin")
        print("5. Exit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            print(f"current balance: {balance}" )
        elif choice==2:
            amount=int(input("Enter deposit amount:"))
            if amount>0:
                balance=balance+amount
                print(f"current balance:{balance}")
                
            else:
                print("Invalid Amount")
        elif choice==3:
            amount=int(input("Enter Amount:"))
            
            if amount>balance:
                print("Insufficiant balance")
            elif amount>0:
                 balance=balance-amount
                 print("Your withdrawal is successfull")
                 print(f"current balance:{balance}")
 
            else:
                print("Invalid Amount")
        elif choice==4:
            pin=int(input("Enter PIN:"))
            if pin!=correct_pin:
                print("Incorrect PIN")
            else:
                new_pin=int(input("New PIN:"))
                confirm_pin=int(input("Confirn PIN:"))
                if new_pin!=confirm_pin:
                    print("PIN doesnt match")
                else:
                    correct_pin=new_pin
                    print("PIN updated successfully")
        elif choice==5:
            print("Thanks for visiting Python ATM")
            break
        elif choice>5:
            print("Choose between 1 t0 5")
                
                
                
            
                    
            
        
            
            
