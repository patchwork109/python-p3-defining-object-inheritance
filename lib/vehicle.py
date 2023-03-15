class Vehicle:

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        print("vrrrrrrrooom!")
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        print("filling up!")
        return "filling up!"

# fiat = Vehicle("small", 4)
# fiat.go()
# fiat.fill_up_tank()
