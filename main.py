from bank import Bank
from person import User,Admin

def main():
    bank = Bank("Pubali",'Uttara')
    kuddos = User('Kuddos Khan',bank)
    bank.add_user(kuddos)
    moin = User("Moin uddin",bank)
    bank.add_user(moin)
    kuddos.deposite(1000)
    moin.deposite(2000)
    kuddos.deposite(2000)
    kuddos.withdraw(1500)
    kuddos.take_loan(2000)
    kuddos.transfer(1000,moin)

    akib = Admin("Akib Hasan",bank)
    bank.add_admin(akib)
    akib.loan_feature(True)
    akib.total_loan()
    akib.total_bank_balance()
    akib.loan_feature(False)
    kuddos.take_loan(100)
    moin.transfer(100,kuddos)
    kuddos.transection_history()
    
    print(bank)
    print("git")

if __name__ == '__main__':
    main()
