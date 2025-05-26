import re
import json
class BankManagement:
    def __init__(self):
        self.welcome_window()
        
    def valid_phone_no(self):
        phone = input("phone no   :    ")
        
        if phone.isdigit() and len(phone) == 10:
            return phone
        
        else:
            print("please insert valid phone number")
            exit()

    def bring_data_from_db(self):
        with open('database.json', 'r') as f:
            database = json.load(f)
        return database              

    def check_password_strength(self) -> str:
        password = input("password   :    ")

        strong_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[^\s]{8,}$'
      
        if re.match(strong_pattern, password):
            return password
        else:
            print("❌ Weak password detected!")
            exit()
            
        
    def is_valid_email(self):
        email =  input("email      :    ")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Use re.match to check if the pattern matches the email
        if re.match(email_regex, email) is not None:
            return email
        else:
            print("Pleas insert a valid email")
            exit()
        
    def generate_account_no(self):
        import random
        digits = "0123456789"
        return ''.join(random.choices(digits, k = 7))

    def loginWindow(self):
        self.login_account_no = input("Account Number: ")
        self.login_password = input("Password: ")

        database =  self.bring_data_from_db
        
        
        if self.login_account_no in database.keys(): # Check if your account number in database
            db_password = database[self.login_account_no]["password"] # Password from database
            user_info = database[self.login_account_no]
            if self.login_password == db_password: # Checking if login password matched with your database password
                cap = CustomerAccessPortal(self.login_account_no, user_info)
            else:
                print("wrong password")
                print("exitting the app.............")
                exit()
        else:
            print("no such account exists")
            print("exitting the app.............")
            exit()



    def welcome_window(self):
        print("-------------------Welcome Window---------------")
        choice = input("""
            1 : Sign Up
            2 : Login
            3 : Exit        
        """)

        if choice == "1":
            self.signUpWindow()

        elif choice == "2":
            self.loginWindow()

        elif choice == "3":
            exit()

    
    def signUpWindow(self):
        database = self.bring_data_from_db()
            
        user_info = { 
                            "name"         : input("name       :    "),
                            "dob"          : input("dob        :    "),
                            "phone"        : self.valid_phone_no(),
                            "address"      : input("address    :    "),
                            "email"        : self.is_valid_email(),
                            "password"     : self.check_password_strength(),
                            "adhaar no"    : input("adhaar no  :    "),                           
                            "balance"      : 0
                 }
            
        database.update({self.generate_account_no() : user_info})
        
        
        with open('database.json', 'w') as f:
            json.dump(database, f)
 
        print("Account succesfully Created. Info= ", user_info) 
        
        


class CustomerAccessPortal:
    def __init__(self, account_no, user_info):
        self.acc_no = account_no
        self.user_info = user_info
        self.customer_window()

    def check_balance(self):
        return self.user_info["balance"]
    
    def withdraw_amount(self):
        pass

    def deposit_amount(self):
        pass

    def balance_transfer(self):
        pass

    def customer_window(self):
        print("-------------This is the customer window -------------")
        choice = input ("""
                        1: Check balance
                        2: Withdraw
                        3: Deposit
                        4: Balance Transfer
                        5: exit
                        """)
        if choice == '1':
            print("Your current balance = ", self.check_balance)

        elif choice == '2':
            self.withdraw_amount()

        elif choice == '3':
            self.deposit_amount()

        elif choice == '4':
            self.balance_transfer()

        elif choice == '5':
            exit()
    