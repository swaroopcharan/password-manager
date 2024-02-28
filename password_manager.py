from cryptography.fernet import Fernet

# def key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#key()                   run this first time to get key file

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter the Master Password: ")
key = load_key()
fer = Fernet(key)

def view(): #helps you to view all your passwords
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(" | ")
            print(f"User: {user} | Password: {fer.decrypt(password.encode()).decode()}")

def add(): # this function helps you to add accounts to your password manager
    name = input("Account name: ")
    pwd = input("Account password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n") 

while True:
    if master_pwd == "charan": # change this to your master password
        mode = input("Would you like to Add new password or View existing passwords? (Add/View), (press q to quit): ")
        if mode.lower() == "q":
            break

        if mode.lower() == "add":
            add()
        elif mode.lower() == "view":
            view()
        else:
            print("Invalid input")
            continue
    else:
        print("Invalid Master Password")
        break