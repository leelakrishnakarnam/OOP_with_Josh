class Guest:
    def __init__(self, last, first, rank, age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = int(age)

    def guest_information(self, all_guests):
        for guest in all_guests:
            print(f"{guest.first_name}, {guest.last_name}, Age: {guest.age}")
    
    def loyalty_program(self, all_guests):
        # Gold Member >= 10
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        if gold_members:
            print(f"Gold Members:")        
            for member in gold_members:
                print(f"\tGuest: {member}")

    def guest_average(self, all_guests):
        total_age = 0
        for guest in all_guests:
            total_age += guest.age
        avg_age = total_age / len(all_guests)
        print(f"Average customer age: {avg_age}")





all_guests = list()
num_guests = int(input("Enter a number of guests: "))
for i in range(num_guests):
    data = input("First Name/Last Name/Rank/Age: ").split("/")
    guest = Guest(data[0], data[1], int(data[2]), int(data[3]))
    # data = ["John", "Doe", "8", "45"]
    all_guests.append(guest)

guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_information(all_guests)
guest.guest_average(all_guests)

