class App:
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username

    def login(self):
        if self.username == "Kittu" and self.users >= 1:
            print(f"Welcome, {self.username}")
            print(f"Your storage is: {self.storage}")
        else:
            print(f"Access denied!")
    
    def increase_capacity(self, number):
        self.storage += number
        print(f"Updated storage: {self.storage}")

    def check_upgrade(self):
        if self.users >= self.storage:
            upgrade_amount = int(input("Upgrade amount: "))
            self.storage += upgrade_amount
        else:
            print(f"You still have: {self.storage - self.users} spaces open!")

product_one = App(35, 256, "Kittu")
product_one.login()
product_one.increase_capacity(44)
print()
product_two = App(12, 128, "Leela")
product_two.login()
product_two.check_upgrade()
