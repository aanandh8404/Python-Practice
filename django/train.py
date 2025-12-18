class User:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

class main:
    def __init__(self):
        self.users = []

    def searchUser(self):
        name = input("Enter name :")
        for i in self.users:
            if i.name == name:
                print(f"name :{i.name}, age : {i.age}")

    def menu(self):
        while True:
            print("\n------------Menu------------+")
            print("1.Add User")
            print("2.Search user")
            choice = int(input("\nChoose option :"))
            
            if choice == 1:
                name = input("\nEnter User name :")
                age = int(input("Enter age :"))
                address = input("Enter Address :")
                print("Added successfully")

                self.users.append(User(name,age,address))
            
            if choice == 2:
                self.searchUser()

system = main()
system.menu()