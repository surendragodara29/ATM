Total_Amount = 10_00_000

Withdraw = int(input("Enter the Amount: "))

if Total_Amount > Withdraw:
    print(f"₹{Withdraw} credited from Account")
    Balance = Total_Amount - Withdraw
    print(f"₹{Balance} left")
    while True:
        choice = input("you want to credit more money? (yes/no): ")
        if choice == "yes":
            Credit = int(input("Enter the Amount to Credit: "))
            Balance = Balance - Credit
            print(f"₹{Credit} credited to Account")
            print(f"₹{Balance} is your new Balance")
        elif choice == "no" :
            print("The End!\n Thank you!")
            break

        else:
            print("Response not defined!")

else:
    print("Insufficient Balance")