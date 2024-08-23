#sign up



account = input("Enter your username: ")
password = input("Enter your password: ")

print("your username is" + " " + account)
print("your password is" + " " + password)

#deposit

deposit = 2000

bank_deposit = int(input("Enter your deposit: "))

if bank_deposit == 2000:
    print("succesful your deposit working")
elif bank_deposit != 2000:
    print("unsuccesfull Try again")  

#withdraw

withdraw = 1000

bank_withdraw = int(input("Enter your withdraw: "))

if bank_withdraw == 1000:
    print("withdrwar succesful wait your request working")
elif bank_withdraw != 1000:
    print("unsuccesful please Try again")

#exit

print("Exiting the system. Thank you for banking with us!")