# PROJECT 18 - TRAIN RESERVATION SYSTEM
# Concepts:
# Lists, Dictionaries, Functions, OOP

class TrainReservationSystem:
    def __init__(self):
        # LIST + DICTIONARIES
        self.trains = [
            {
                "train_no": "12001",
                "train_name": "Shatabdi Express",
                "source": "Lucknow",
                "destination": "Delhi",
                "fare": 850,
                "total_seats": 50,
                "available_seats": 50
            },
            {
                "train_no": "12555",
                "train_name": "Gorakhdham Express",
                "source": "Gorakhpur",
                "destination": "Delhi",
                "fare": 700,
                "total_seats": 60,
                "available_seats": 60
            },
            {
                "train_no": "12230",
                "train_name": "Lucknow Mail",
                "source": "Lucknow",
                "destination": "Mumbai",
                "fare": 1200,
                "total_seats": 80,
                "available_seats": 80
            },
            {
                "train_no": "12310",
                "train_name": "Rajdhani Express",
                "source": "Delhi",
                "destination": "Kolkata",
                "fare": 1500,
                "total_seats": 70,
                "available_seats": 70
            }
        ]
        # LIST OF BOOKINGS
        self.bookings = []

        # Ticket number
        self.next_ticket_no = 1001

    # DISPLAY TRAINS
    def display_trains(self):
        print("\n========== AVAILABLE TRAINS ==========")
        for train in self.trains:
            print("------------------------------------------")
            print("Train No       :", train["train_no"])
            print("Train Name     :", train["train_name"])
            print("From           :", train["source"])
            print("To             :", train["destination"])
            print("Fare           : Rs.", train["fare"])
            print("Available Seat :", train["available_seats"])

    # SEARCH TRAIN
    def search_train(self):
        print("\n========== SEARCH TRAIN ==========")
        source = input("Enter Source: ").strip().lower()
        destination = input("Enter Destination: ").strip().lower()
        found = False
        for train in self.trains:
            if (
                train["source"].lower() == source
                and
                train["destination"].lower() == destination
            ):
                found = True

                print("\nTrain Found!")
                print("------------------------------------------")
                print("Train No       :", train["train_no"])
                print("Train Name     :", train["train_name"])
                print("From           :", train["source"])
                print("To             :", train["destination"])
                print("Fare           : Rs.", train["fare"])
                print("Available Seat :", train["available_seats"])
        if not found:
            print("\nNo train found for this route.")

    # FIND TRAIN
    def find_train(self, train_no):
        for train in self.trains:
            if train["train_no"] == train_no:
                return train
        return None

    # CALCULATE FARE
    def calculate_fare(self, train, number_of_seats):
        fare = train["fare"] * number_of_seats
        return fare
        
    # BOOK TICKET
    def book_ticket(self):
        print("\n========== BOOK TICKET ==========")
        train_no = input("Enter Train Number: ")
        train = self.find_train(train_no)
        if train is None:
            print("Train not found.")
            return
        
        print("\nTrain Details")
        print("------------------------------------------")
        print("Train Name :", train["train_name"])
        print("Route      :", train["source"], "->", train["destination"])
        print("Fare       : Rs.", train["fare"])
        print("Available  :", train["available_seats"])

        if train["available_seats"] == 0:
            print("\nNo seats available.")
            return

        name = input("\nEnter Passenger Name: ")
        age = int(input("Enter Passenger Age: "))

        number_of_seats = int(
            input("Enter Number of Seats: ")
        )

        # Check seats
        if number_of_seats <= 0:
            print("Invalid number of seats.")
            return

        if number_of_seats > train["available_seats"]:
            print(
                "Only",
                train["available_seats"],
                "seats are available."
            )
            return

        # Calculate fare
        total_fare = self.calculate_fare(
            train,
            number_of_seats
        )

        # Create booking dictionary
        booking = {
            "ticket_no": self.next_ticket_no,
            "train_no": train["train_no"],
            "train_name": train["train_name"],
            "passenger_name": name,
            "age": age,
            "seats": number_of_seats,
            "fare": total_fare
        }

        # Add booking to list
        self.bookings.append(booking)

        # Reduce available seats
        train["available_seats"] -= number_of_seats

        # Increase ticket number
        self.next_ticket_no += 1

        print("\n========== TICKET BOOKED ==========")
        print("Ticket Number :", booking["ticket_no"])
        print("Passenger Name:", booking["passenger_name"])
        print("Train         :", booking["train_name"])
        print("Seats         :", booking["seats"])
        print("Total Fare    : Rs.", booking["fare"])
        print("===================================")

    # DISPLAY BOOKINGS
    def display_bookings(self):
        print("\n========== ALL BOOKINGS ==========")

        if len(self.bookings) == 0:
            print("No bookings found.")
            return

        for booking in self.bookings:

            print("------------------------------------------")
            print("Ticket Number :", booking["ticket_no"])
            print("Passenger     :", booking["passenger_name"])
            print("Age           :", booking["age"])
            print("Train Number  :", booking["train_no"])
            print("Train Name    :", booking["train_name"])
            print("Seats         :", booking["seats"])
            print("Fare          : Rs.", booking["fare"])

    # CANCEL TICKET
    def cancel_ticket(self):
        print("\n========== CANCEL TICKET ==========")

        ticket_no = int(
            input("Enter Ticket Number: ")
        )
        for booking in self.bookings:
            if booking["ticket_no"] == ticket_no:
                train = self.find_train(
                    booking["train_no"]
                )

                # Return seats to train
                train["available_seats"] += booking["seats"]

                # Remove booking
                self.bookings.remove(booking)

                print("\nTicket cancelled successfully!")
                print("Ticket Number :",
                      ticket_no)
                print("Refund Amount : Rs.",
                      booking["fare"])
                return
        print("\nTicket not found.")

    # CHECK AVAILABLE SEATS
    def check_seats(self):
        print("\n========== CHECK AVAILABLE SEATS ==========")

        train_no = input("Enter Train Number: ")
        train = self.find_train(train_no)
        if train is None:
            print("Train not found.")
            return

        print("\nTrain Name :", train["train_name"])
        print("Route      :", train["source"],
              "->", train["destination"])
        print("Available Seats :",
              train["available_seats"])

    # MAIN MENU
    def menu(self):
        while True:
            print("\n")
            print("==========================================")
            print("       TRAIN RESERVATION SYSTEM")
            print("==========================================")

            print("1. Display All Trains")
            print("2. Search Train")
            print("3. Check Available Seats")
            print("4. Book Ticket")
            print("5. Display Bookings")
            print("6. Cancel Ticket")
            print("7. Exit")

            print("==========================================")

            choice = input("Enter Your Choice: ")
            if choice == "1":
                self.display_trains()
            elif choice == "2":
                self.search_train()
            elif choice == "3":
                self.check_seats()
            elif choice == "4":
                self.book_ticket()
            elif choice == "5":
                self.display_bookings()
            elif choice == "6":
                self.cancel_ticket()
            elif choice == "7":

                print("\nThank you for using")
                print("Train Reservation System!")
                break
            else:
                print("\nInvalid choice!")
                print("Please select 1-7.")

# MAIN PROGRAM
system = TrainReservationSystem()
system.menu()