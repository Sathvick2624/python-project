import random
while True:
    print("\nGuess a Number between 0 to 100")
    secret_number=random.randint(0,100)
    count=0
    while True:
    

        user=guess=int(input("Enter a number: "))
        if guess<0 or guess>100:
            print("Please enter a number between 0 to 100")
            continue
        count=count+1
        if guess==secret_number:
            print("Congratulations\nYou guessed it in",count,"attempts")
            break
    
        if guess<secret_number:
            print("Too Low!")
        else:
            print("Too High!")

        
    choice=input("do you wanna play again?(y/n):").lower()
    if choice=="n":
        print("Thanks for playing.")
        break
    
    elif choice!="y":
        print("invalid choice")
        break
      
    
    
