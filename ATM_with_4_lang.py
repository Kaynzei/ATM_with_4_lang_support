import os
import platform
from googletrans import Translator

class ATM:
    def __init__(self):
        self.language = "English"
        self.account_balance = 10000.0  # Initial account balance
        self.selected_option = None
        self.slip_data = ""
        self.translator = Translator()

    def select_language(self):
        print("Select your language:")
        print("1. English")
        print("2. Igbo")
        print("3. Hausa")
        print("4. Yoruba")
        choice = input("Enter your choice: ")
        languages = ["English", "Igbo", "Hausa", "Yoruba"]
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 4:
                self.language = languages[choice - 1]
        except ValueError:
            print("Invalid choice. Using English by default.")

    def check_balance(self):
        message = f"Your account balance is: {self.account_balance}"
        translated_message = self.translator.translate(message, dest=self.language).text
        print(translated_message)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.account_balance:
            self.account_balance -= amount
            message = f"Withdrawal successful. Remaining balance: {self.account_balance}"
        else:
            message = "Insufficient funds."
        translated_message = self.translator.translate(message, dest=self.language).text
        print(translated_message)

    def transfer_money(self):
        recipient = input("Enter recipient's account number: ")
        amount = float(input("Enter amount to transfer: "))
        if amount <= self.account_balance:
            self.account_balance -= amount
            message = f"Transfer of {amount} to {recipient} successful. Remaining balance: {self.account_balance}"
        else:
            message = "Insufficient funds."
        translated_message = self.translator.translate(message, dest=self.language).text
        print(translated_message)

    def print_slip(self):
        self.slip_data += f"Account Balance: {self.account_balance}\n"
        file_name = "ATM_Slip.txt"
        with open(os.path.join(os.path.expanduser('~'), 'Documents', file_name), "w") as file:
            file.write(self.slip_data)
        message = f"Transaction slip saved as {file_name} in Documents folder."
        translated_message = self.translator.translate(message, dest=self.language).text
        print(translated_message)

    def cancel(self):
        message = "Transaction canceled."
        translated_message = self.translator.translate(message, dest=self.language).text
        print(translated_message)

    def exit(self):
        message = "Exiting ATM. Thank you for using our services."
        translated_message = self.translator.translate(message, dest=self.language).text
        print(translated_message)

    def run(self):
        print("Welcome to Kay's microfinance Bank Teller Machine")
        self.select_language()
        while True:
            print("\nATM Menu:")
            menu_items = ["Check Balance", "Withdraw", "Transfer Money", "Print Slip", "Cancel", "Exit"]
            for i, item in enumerate(menu_items, 1):
                message = f"{i}. {item}"
                translated_message = self.translator.translate(message, dest=self.language).text
                print(translated_message)
            choice = input("Enter your choice: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.transfer_money()
            elif choice == "4":
                self.print_slip()
            elif choice == "5":
                self.cancel()
                break
            elif choice == "6":
                self.exit()
                break
            else:
                message = "Invalid choice. Please try again."
                translated_message = self.translator.translate(message, dest=self.language).text
                print(translated_message)


if __name__ == "__main__":
    # Detect the operating system
    operating_system = platform.system()
    print(operating_system)
        
    
    # Initialize the ATM
    atm = ATM()

    # Run the ATM
    atm.run()
