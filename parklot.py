class ParkSpace:
    def __init__(self, id: int) -> None:
        self.id = id
        self.empty = True
        self.car_id = None

class ParkLot:
    def __init__(self, size: int = 100) -> None:
        self.size = size
        self.empty_park_space_list = [ParkSpace(id) for id in range(0, size)]
        self.filled_park_space_map = {}

    def park(self, car_id) -> int:
        if not self.empty_park_space_list:
            print("There is no remaining parking space")
            return -1
        park_space = self.empty_park_space_list.pop()
        park_space.car_id = car_id
        park_space.empty = False
        self.filled_park_space_map[park_space.id] = park_space
        print(f'Successfully park car with id {car_id}, please remenber your parking space id: {park_space.id}')
        return park_space.id

    def pick_up(self, car_id, park_space_id) -> bool:
        if park_space_id not in self.filled_park_space_map:
            print(f'There is no car in park space {park_space_id}')
            return False
        park_space = self.filled_park_space_map[park_space_id]
        if park_space.car_id != car_id:
            print(f'Car Id does not matched in park space {park_space_id}')
            print(f'Your car id: {car_id} not matched car id in the space {park_space.car_id}')
            return False
        park_space.car_id = None
        park_space.empty = True
        self.empty_park_space_list.append(park_space)
        self.filled_park_space_map.pop(park_space_id)
        print(f'Successfully pick up car with id {car_id}')
        return True

park_lot = ParkLot(size=100)

print("===========Parking Car===========")

park_space_id_99 = park_lot.park(car_id=7575)
park_space_id_98 = park_lot.park(car_id=6767)
park_space_id_97 = park_lot.park(car_id=5252)

print("===========Picking up===========")

# Test pick up right car
park_lot.pick_up(car_id=7575, park_space_id=park_space_id_99)

# Test pick up in empty 
park_lot.pick_up(car_id=6767, park_space_id=park_space_id_99)

# Test pick up wrong car
park_lot.pick_up(car_id=6767, park_space_id=park_space_id_97)
