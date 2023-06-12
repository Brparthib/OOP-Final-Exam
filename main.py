from Admin import Admin
from User import User

def main():
    belal = User('1111', 'Belal', 'belal@gmail.com', '4321') # User
    belal.create_account('1111', 'Belal', 'belal@gmail.com', '4321') # User
    belal.deposit(5000)
    belal.check_balance() # User

    helal = User('1112', 'helal', 'helal@gmail.com', '4322') # User
    helal.create_account('1112', 'helal', 'helal@gmail.com', '4322') # User

    
    belal.deposit(4000) # User

    kuddus = Admin('1234', 'Kuddus', 'kuddus@gmail.com', '5432') # Admin
    kuddus.create_account('1234', 'Kuddus', 'kuddus@gmail.com', '5432') # Admin
    kuddus.check_total_balance() # Admin

    helal.deposit(30000) # User
    helal.check_balance() # User

    kuddus.check_total_balance() # Admin

    sakib = Admin('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.create_account('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.check_total_balance() # Admin

    helal.check_balance() # User

    helal.withdraw(1000) # User
    helal.check_balance() # User

    helal.transfer(belal, 5000) # User
    belal.check_balance() # User

    sakib.check_transaction() # Admin
    sakib.check_total_balance() # Admin

    belal.take_loan(5000) # User
    belal.check_balance() # User

    sakib.check_total_balance() # Admin

    helal.check_balance() # User

    kuddus.toggle_loan_feature(False) # Admin

    belal.take_loan(5000) # User
    helal.take_loan(5000) # User
    helal.check_balance() # User
    belal.check_balance() # User

    kuddus.check_total_loan() # Admin
    kuddus.check_transaction() # Admin

    belal.check_transaction_history() # User
    helal.check_transaction_history() # User

if __name__ == '__main__':
    main()
