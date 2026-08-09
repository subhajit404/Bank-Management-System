## Improvise Version

import json
import random
import string
from pathlib import Path


class Bank:
    DATABASE = Path("data.json")

    def __init__(self):
        self.data = self.load_data()

    # -----------------------------
    # Load data from JSON
    # -----------------------------
    def load_data(self):
        try:
            if self.DATABASE.exists():
                with open(self.DATABASE, "r") as file:
                    return json.load(file)

            return []

        except (json.JSONDecodeError, OSError):
            return []

    # -----------------------------
    # Save data to JSON
    # -----------------------------
    def save_data(self):
        try:
            with open(self.DATABASE, "w") as file:
                json.dump(self.data, file, indent=4)

        except OSError as error:
            raise Exception(f"Unable to save data: {error}")

    # -----------------------------
    # Generate account number
    # -----------------------------
    def generate_account_number(self):
        while True:
            letters = ''.join(
                random.choices(string.ascii_uppercase, k=3)
            )

            numbers = ''.join(
                random.choices(string.digits, k=3)
            )

            special = random.choice("!@#$%^&*")

            account_no = letters + numbers + special

            if not any(
                user["accountNo"] == account_no
                for user in self.data
            ):
                return account_no

    # -----------------------------
    # Find account
    # -----------------------------
    def find_account(self, account_no, pin):
        for user in self.data:
            if (
                user["accountNo"] == account_no
                and user["pin"] == pin
            ):
                return user

        return None

    # -----------------------------
    # Create account
    # -----------------------------
    def create_account(self, name, age, email, pin):

        if age < 18:
            return False, "You must be at least 18 years old."

        if not pin.isdigit() or len(pin) != 4:
            return False, "PIN must contain exactly 4 digits."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account_number(),
            "balance": 0
        }

        self.data.append(account)
        self.save_data()

        return True, account

    # -----------------------------
    # Deposit money
    # -----------------------------
    def deposit(self, account_no, pin, amount):

        user = self.find_account(account_no, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Deposit amount must be greater than 0."

        if amount > 10000:
            return False, "Maximum deposit is ₹10,000."

        user["balance"] += amount
        self.save_data()

        return True, f"₹{amount} deposited successfully."

    # -----------------------------
    # Withdraw money
    # -----------------------------
    def withdraw(self, account_no, pin, amount):

        user = self.find_account(account_no, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."

        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount
        self.save_data()

        return True, f"₹{amount} withdrawn successfully."

    # -----------------------------
    # Get account details
    # -----------------------------
    def get_details(self, account_no, pin):

        user = self.find_account(account_no, pin)

        if user is None:
            return None

        return user.copy()

    # -----------------------------
    # Update account
    # -----------------------------
    def update_account(
        self,
        account_no,
        pin,
        name=None,
        email=None,
        new_pin=None
    ):

        user = self.find_account(account_no, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        if name:
            user["name"] = name

        if email:
            user["email"] = email

        if new_pin:

            if not new_pin.isdigit() or len(new_pin) != 4:
                return False, "PIN must contain exactly 4 digits."

            user["pin"] = new_pin

        self.save_data()

        return True, "Account details updated successfully."

    # -----------------------------
    # Delete account
    # -----------------------------
    def delete_account(self, account_no, pin):

        user = self.find_account(account_no, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        self.data.remove(user)
        self.save_data()

        return True, "Account deleted successfully."