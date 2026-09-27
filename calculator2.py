while True:
    print("\n Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice=input("Enter your choice between (1-5):")


    if choice=="5":
        print("Good Bye!")
        break
    if choice>"5":
        print("Invalid Choice!")
        continue

    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))


    if choice=="1":
        print("Answer=",num1+num2)

    elif choice=="2":
        print("Answer=",num1-num2)
    elif choice=="3":
        print("Answer=",num1*num2)
    elif choice=="4":
        if num2==0:
            print("cannot divide")
        else:
            print("Answer=",num1/num2)
    
        
        
    
