class Atm:


    def __init__(self):

        self.__pin = ""
        self.__balance = 0
        
        self.menu()


    def get_pin(self):
        return self.__pin



    def set_pin(self,new_pin):

        if type(new_pin)==str:
            
            self.__pin = new_pin
            print("pin changed")
        else:
            return "not allowed"

    
        
    

    def menu(self): 
        user_input = input("""
                        hello how would you like to proceed ?
                            1. Enter 1 to correct pin 
                            2. Enter 2 to deposit
                            3. enter 3 to withdraw
                            4. enter 4 to check the balance
                            5. enter 5 to exit

                        
""")
        if user_input == "1":
            self.create_pin()
        elif user_input =="2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            return "bye"
        


    def create_pin(self):
        self.__pin = input("enter your pin")
        print("pin set sucessfuly")

    def deposit(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter your amount"))
            self.__balance = self.__balance+amount
            print("sucesseful")
        else:
            print("invalid pin")
    
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter your amount"))
            if amount < self.__balance:
                self.__balance = self.__balance-amount
                print("sucesseful")
            else:
                print("balance not sufficient")
            
        else:
            print("invalid pin")


    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")

sbi=Atm()
