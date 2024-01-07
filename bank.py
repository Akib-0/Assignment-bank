class Bank:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.users = {}
        self.admins = {}
        self.loan = True
        self.total_loan_taken = 0
        self.total_balance = 0
        self.transections = {}
 
    def add_user(self,user):
        self.users[user.name] = user
    
    def add_admin(self,admin):
        self.admins[admin.name] = admin

    def __repr__(self):    
        print("------USERS--------")
        for user in self.users.values():
            print(f'{user.name} have {user.balance}')
        print("-------ADMINS---------")
        for admin in self.admins.values():
            print(admin.name)
        return ''