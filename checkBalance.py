# checking balance function: no need to include in the minibanking file
def check_balance(self):
        return self.balance

def check_balance():
    if current_user:
        print(f"Your current balance is: {current_user.check_balance()}")
    else:
        print("You must be signed in to perform this action.")