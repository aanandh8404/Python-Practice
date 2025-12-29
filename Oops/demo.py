class Laptop:
    def details(self,brand, ram):
        print([brand, ram])

lap1 = Laptop()
lap2 = Laptop()

lap1.details("Dell","16gb")
lap1.details("HP","8gb")