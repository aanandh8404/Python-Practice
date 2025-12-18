class Train:
    def __init__(self,train_no, name, source, destination, seats, fare):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

class TrainBookingSystem:

    def __init__(self):
        self.trains = []
        self.bookings = {}
        self.booking_id = 1000
        self.add_trains()

    def add_trains(self):
        self.trains.append(Train(101,"train1","Chennai","Coimbatore",400,500))
        self.trains.append(Train(102,"train2","Chennai","Bangalore",800,700))
        self.trains.append(Train(103, "train3","Chennai","Hyderabad",500,600))

    def view_trains(self):
        print("\nAvailable Trains :")
        for t in self.trains:
            print(f"Train no : {t.train_no} | Name : {t.name} | Source : {t.source} | Destination : {t.destination} | Seats Available : {t.seats} | fare : {t.fare}")

    def book_train(self):
        self.view_trains()
        train_no = int(input("\nEnter Train no to book :"))
        no_of_seats = int(input("Enter the number of seats to book :"))
        for t in self.trains:
            if t.train_no == train_no:
                if t.seats >= no_of_seats:
                    self.booking_id += 1
                    t.seats -= no_of_seats
                    self.bookings[self.booking_id] = t
                    print("Booking successfull")
                    break
                else:
                    print("No seats Available")
        else:
            print("Invalid train no")

    def view_booked(self):
        print("\n--------------Booked trains--------------")
        for b in self.bookings:
            train = self.bookings[b]
            print("Booking id : ",b)
            print("Train no : ",train.train_no)
            print("Train Name : ",train.name)
            print("From  : ",train.source)
            print("To  : ",train.destination)
            print("Price : Rs.",train.fare)

    def cancel_ticket(self):
        b_id = int(input("Enter Booking id of Train to be Cancelled :"))
        for b in self.bookings:
            if b == b_id:
                del self.bookings[b]
                print("Ticket Cancelled successfully")
                break
        else :
            print("Invalid Booking id")

    def menu(self):
        while True:
            print("\nTrain Ticket Booking system")
            print("1.View Trains")
            print("2.Book Train")
            print("3.View Booked Trains")
            print("4.Cancel train")
            print("5.Exit")

            choice = int(input("Enter your Choice (1 - 5) :"))

            if choice == 1:
                self.view_trains()
            elif choice == 2:
                self.book_train()
            elif choice == 3:
                self.view_booked()
            elif choice == 4:
                self.cancel_ticket()
            elif choice == 5:
                print("Thank You")
                break

            else :
                print("Invalid Choice")

system = TrainBookingSystem()
system.menu()
            