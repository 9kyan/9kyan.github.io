class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers =[]

    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(5)
people =["小辣椒","小广","小和","HHJ"]

for person in people:
    if flight.add_passengers(person):
        print(f"{person} 上了飞机，哈哈")
    else:
        print(f"{person}, 上不了飞机了吧，滚蛋吧")