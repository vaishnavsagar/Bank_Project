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
        print("this is the login window")

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
        with open('database.json', 'r') as f:
            database = json.load(f)
            
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
        
