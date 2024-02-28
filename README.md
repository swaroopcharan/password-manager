Certainly! Below is a README file for your script:

---

# Password Manager using Python

This Python script serves as a simple password manager utilizing encryption for added security. It allows users to store and view passwords for various accounts.

## Setup

1. **Generate Key**: Run the `key()` function once to generate the encryption key. This key is stored in a file named `key.key`.

```python
from cryptography.fernet import Fernet

def key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
```

2. **Load Key**: Load the encryption key from the `key.key` file using the `load_key()` function.

```python
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
```

3. **Run the Script**: Execute the script and enter the master password when prompted. The default master password is set to "charan" (change it as needed).

```python
master_pwd = input("Enter the Master Password: ")
```

## Functionality

- **View Passwords**: Use the `view()` function to display all stored passwords.

```python
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(" | ")
            print(f"User: {user} | Password: {fer.decrypt(password.encode()).decode()}")
```

- **Add Passwords**: Utilize the `add()` function to add new accounts to the password manager.

```python
def add():
    name = input("Account name: ")
    pwd = input("Account password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n") 
```

## Usage

- When prompted, enter the master password (default is "charan").
- Choose to either add a new password or view existing passwords.
- Type "q" to quit the program.

## Note

- Ensure to keep the master password secure.
- Backup the `key.key` file to avoid losing access to stored passwords.

---

Feel free to customize and enhance the README as needed. Let me know if you need further assistance or modifications!