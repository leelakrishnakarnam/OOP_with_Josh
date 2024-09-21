class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.month = int(month)
        self.type = type
        self.price = 0

    def trip_information(self):
        if self.month >= 10 and self.month <= 3:
            print(f"You are going to {self.country} in the winter! This is a {self.type} trip!")
        elif self.month > 3 and self.month < 10:
            print(f"You are going to {self.country} in the Summer! This is a {self.type} trip!")
        else:
            print(f"invalid Input!")

    def calculate_cost(self, cost):
        costs = []
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter another cost: "))

        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice, inspect

    def advice(self, number):
        if number < 500:
            print(f"Low budget!")
        elif number >= 500 and number < 1500:
            print(f"Take a flight to anywhere...")
        else:
            print(f"Luxury Trip!")

    def list_inspect(self, costs):
        less_than_ten = 0
        for i in costs:
            if i >= 10:
                less_than_ten += 1
        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated price: {self.price}")

location = input("Enter a country: ").capitalize()
trip_type = input("Leisure or Business: ").capitalize()
month = input("Enter a month: ")

test = Travel(location, month, trip_type)
test.trip_information()

flight_cost = int(input("Enter flight cost: "))
test.calculate_cost(flight_cost)