from datetime import datetime
from linecache import getline


class BRFP(object):
    def __init__(self, how_many_bikes, time_type, id):
        self.bikes = how_many_bikes
        self.time_type = time_type
        self.id = id
        with open("White Stocks", "r") as f:
            x = f.read()
        self.stock = x
        self.cost_h = 6
        self.cost_d = 20
        self.cost_w = 60
        with open(f"{self.id}", "w") as b:
            b.write(str(self.bikes))
            b.write(self.time_type)

    def new_bikes(self, new_bikes):
        self.bikes = new_bikes

    def new_time_type(self, new_type_time):
        self.time_type = new_type_time

    def new_name(self, new_id):
        self.id = new_id

    def stock(self):
        if self.stock >= self.bikes:
            with open(f"{self.id}", "ab") as lkf:
                lkf.write(self.bikes)
        else:
            if self.stock > str(0):
                print(f" > we currently only have {self.stock}...")
                new_value = input(" > Do you want to assign the bikes to a new value ? (Y/N) \n > ")
                if new_value == "Y" or new_value == "y":
                    new_bike = int(input(" > How many bikes do you need ? \n > "))
                    BRFP.new_bikes(new_bikes=new_bike)
                    with open("White Stocks", "w") as kf:
                        kf.write("\n")
                        kf.write(int(self.stock) - int(new_bike))
                    with open(f"{self.id}", "ab") as lkf:
                        lkf.write("\n")
                        lkf.write(new_bike)
                    print(" > Enjoy your bikes ! ")
                else:
                    print(" > Thank you for stopping bye... \n Thank you....")
                    quit()
            else:
                print(" > The stocks are unavailable.... \n > We are so sorry....")
                quit()

    def cost(self):
        if self.time_type == "H" or self.time_type == "h":
            how_many_h = int(input(" > How many hours do you want to rent a bike for ? \n > "))
            if how_many_h > self.cost_h:
                ms = how_many_h * self.cost_h
                with open(f"{self.id}", "a") as lk:
                    lk.write("\n")
                    lk.write(ms)
            else:
                ms = self.cost_h * how_many_h
                with open(f"{self.id}", "a") as lk:
                    lk.write("\n")
                    lk.write(str(ms))
        elif self.time_type == "D" or "d":
            how_many_d = int(input(" > How many days do you want to rent a bike for ? \n > "))
            if how_many_d > self.cost_d:
                sm = how_many_d * self.cost_d
                with open(f"{self.id}", "a") as lk:
                    lk.write("\n")
                    lk.write(sm)
            else:
                sm = self.cost_h * how_many_d
                with open(f"{self.id}", "a") as lk:
                    lk.write("\n")
                    lk.write(sm)
        else:
            how_many_w = int(input(" > How many weeks do you want to rent a bike for ? \n > "))
            if how_many_w > self.cost_d:
                m = how_many_w * self.cost_d
                with open(f"{self.id}", "a") as lk:
                    lk.write("\n")
                    lk.write(m)
            else:
                m = self.cost_h * how_many_w
                with open(f"{self.id}", "a") as lk:
                    lk.write("\n")
                    lk.write(m)

    def return_bikes(self):
        id = input(" > What is the id that you entered when you rented the bike ? \n > ")
        with open(id, "r") as dk:
            print(getline(dk, 6))

            # 2 = Bikes
            # 4 = Time type
            # 6 = Cost


def start():
    print(" ! > Welcome to DSI Bicycle Shop < ! ")
    di = input(" > What is your id ? \n > ")
    print(" > NOTE : \n YOU SHOULD REMEMBER THE ID TO RETURN THE BIKE !  ")
    choice = ("""
     > B = Buy a Bike
     > R = Rent a Bike
     > What is your choice : \n \n > 
    """)
    print(choice)
    if choice == "B" or choice == "b":
        pass

    elif choice == "R" or "r":
        choices = ("""
         > A = Rent a Bike
         > R = Return a Bike
         > What is your choice  \n \n > 
        """)
        if choices == "A" or choices == "a":
            bikes = int(input(" > How many bikes do you want to buy ? \n > "))
            time = int(input(f" > H = Hours(optional) | D = Days(optional) | W = Weeks(optional) ? \n > "))
            BRFP(how_many_bikes=bikes, time_type=time, id=di)
        else:
            pass
    else:
        print(" > ! INVALID CHOICE ! < ")
        start()


ms = BRFP(how_many_bikes=5, time_type=int("H"), id=int("Ranuga"))
