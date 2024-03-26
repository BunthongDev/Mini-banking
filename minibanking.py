class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    
    ## Checking balance
    def check_balance(self):
        return self.balance

    def check_profile(self):
        return f"Username: {self.username}, Balance: {self.balance}"

accounts = {}
current_user = None

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def sign_up():
    global accounts
    username = input("Enter a username: ")
    if username in accounts:
        print("Username already exists.")
        return
    password = input("Enter a password: ")
    accounts[username] = BankAccount(username, password)
    print("Account created successfully!")

def sign_in():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    account = accounts.get(username)
    if account and account.password == password:
        current_user = account
        print("Signed in successfully!")
    else:
        print("Invalid username or password.")

# display balance
def check_balance():
    if current_user:
        print(f"Your current balance is: {current_user.check_balance()}")
    else:
        print("You must be signed in to perform this action.")

def deposit():
    if current_user:
        amount = get_float_input("Enter the amount to deposit: ")
        if current_user.deposit(amount):
            print("Deposit successful.")
        else:
            print("Deposit failed.")
    else:
        print("You must be signed in to perform this action.")

def withdraw():
    if current_user:
        amount = get_float_input("Enter the amount to withdraw: ")
        if current_user.withdraw(amount):
            print("Withdrawal successful.")
        else:
            print("Withdrawal failed.")
    else:
        print("You must be signed in to perform this action.")

def transfer():
    if current_user:
        target_username = input("Enter the username of the account to transfer to: ")
        target_account = accounts.get(target_username)
        if target_account:
            amount = get_float_input("Enter the amount to transfer: ")
            if current_user.transfer(target_account, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed.")
        else:
            print("Target account not found.")
    else:
        print("You must be signed in to perform this action.")

def check_profile():
    if current_user:
        print(current_user.check_profile())
    else:
        print("You must be signed in to perform this action.")

def logout():
    global current_user
    if current_user:
        current_user = None
        print("Logged out successfully.")
    else:
        print("You are not signed in.")

def main():
    actions = {
        "1": sign_up,
        "2": sign_in,
        "3": check_balance,
        "4": deposit,
        "5": withdraw,
        "6": transfer,
        "7": check_profile,
        "8": logout,
    }
    
    while True:
        print("\nMini Banking System")
        print("1. Sign Up\n2. Sign In\n3. Check Balance\n4. Deposit\n5. Withdraw\n6. Transfer\n7. Check Profile\n8. Logout\n9. Exit")
        choice = input("Choose an action: ")
        if choice == "9":
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
