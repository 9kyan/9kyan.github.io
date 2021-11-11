class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self,name):
        if not self.open_seats():
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = [1,2,3,4]

for person in people:
    if flight.add_passenger(person):
        print(f"{person} 已经上飞机了")
    else:
        print(f"{person} 没有上飞机，因为没有座为了")