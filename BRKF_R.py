import random
import time
import datetime
from datetime import datetime


class RAB(object):
    def __init__(self, id, name, how_many_bikes, time_type, how_much):
        self.id = id
        self.name = name
        self.bikes = int(how_many_bikes)
        self.time_type = time_type
        self.how_muc = how_much
        with open("Rent Stocks", "r") as rs:
            rss = rs.read()
            if FileNotFoundError:
                self.stock = 0
            else:
                self.stock = int(rss)
        with open("H", 'r') as h:
            self.h = int(h.read())
        with open("D", 'r') as d:
            self.d = int(d.read())
        with open("W", "r") as w:
            self.w = int(w.read())

    def new_id(self, new_id):
        self.id = new_id

    def new_name(self, new_name):
        self.name = new_name

    def new_bikes(self, new_bikes):
        self.bikes = new_bikes

    def new_time_type(self, new_time_type):
        self.time_type = new_time_type

    def checking_stock(self):
        if self.stock > self.bikes:
            with open("Rent Stocks", "w") as rs:
                t = self.stock - self.bikes
                rs.write(str(t))
            print(" > Stocks are available...")
            print(" > Processing...")
            time.sleep(10)
        elif self.stock < self.bikes:
            if self.stock > 0:
                print(f" > We don't have {self.bikes}. \n > But we have {self.stock}.")
                new = input(" > Do you want to rent less bikes (Y/N) ? \n > ").upper()
                if new == "Y":
                    new_bikes = input(" > What is the new bike amount ? \n > ")
                    new_bikes = int(new_bikes)
                    if new_bikes < self.stock:
                        n_b = RAB(id=self.id, name=self.name, how_many_bikes=self.bikes, time_type=self.time_type)
                        n_b.new_bikes(new_bikes=new_bikes)
                        with open("Rent Stocks", "w") as rs:
                            t = self.stock - new_bikes
                            rs.write(str(t))
                    elif new_bikes > self.stock:
                        print(f" > You have ordered more bikes than {self.stock} ! \n > Bye Bye ! \n > Try again "
                              f"later....")
                        quit()
                        exit()
                elif new == "N":
                    print(" > Bye Bye... \n > Try again later... \n > Thank you for using our program...")
            elif self.stock < 0:
                print("> We are so sorry \n > if you want to tell us your email.. \n > We can send a email when "
                      "stocks come...")
                want = input(" > Do you want to give us a email address (Y/N) ? \n > ").upper()
                if want == "Y":
                    email = input(" > What is your password ? \n > ")
                    with open("Email.txt", "a") as e:
                        e.write(email)
                        e.write("\n")
                else:
                    print(" > Bye Bye...")
                    quit()
                    exit()

    def price(self):
        global id
        when_pay = input(" > When are you going to pay (R = When returning | N = Now) ? \n > ").upper()
        if when_pay == "R":
            with open(str(f"{self.id}"), "a") as id:
                id.write("UnPaid")
                id.write("\n")
                id.write(self.name)
                id.write("\n")
                now = datetime.now()
                l = now.year, now.month, now.day, now.hour, now.minute, now.second
                id.write(str(l))
                id.write("\n")
                id.write(str(self.bikes))
                id.write("\n")
                if self.time_type == "H":
                    id.write(self.h * self.how_muc)
                elif self.time_type == "D":
                    id.write(self.d * self.how_muc)
                elif self.time_type == "W":
                    id.write(self.w * self.how_muc)
            print(" > Processing...")
            time.sleep(10)
        elif when_pay == "N":
            for_how_many_days = input(" > For how many days are you renting the bike ? \n > ")
            t = int(self.h) * int(for_how_many_days)
            print(f" > THe cost is {t}...")
            credit_Card = input(" > What is the credit card number ? \n > ")
            with open("CC", "w") as io:
                io.write(str(credit_Card))
                io.write("\n")
            with open(str(f"{self.id}"), "a") as id:
                id.write("Paid")  # 1
                id.write("\n")
                id.write(self.name)  # 2
                id.write("\n")
                now = datetime.now()
                l = now.year, now.month, now.day, now.hour, now.minute, now.second
                id.write(str(l))  # 3
                id.write("\n")
                id.write(str(self.bikes))  # 4
                id.write("\n")
                id.write(credit_Card)  # 5
                id.write("\n")
                id.write(str(t))  # 6
                if self.time_type == "H":
                    id.write(self.h * self.how_muc)
                elif self.time_type == "D":
                    id.write(self.d * self.how_muc)
                elif self.time_type == "W":
                    id.write(self.w * self.how_muc)
            print(" > Processing...")
            time.sleep(10)
            random.choice(range(1, 5000))
            l = "Mountain Bike", "Classical Bike", "Supreme Bike"
            random.choice(f"it is a {l}")


class RABR(object):
    def __init__(self, id):
        self.id = id

    def return_bikes(self):
        with open(self.id) as di:
            l = di.readline()
            if l[1] == "Paid":
                with open("Rent Stocks", "w+") as olol:
                    o = olol.read()
                    l = int(o) + int(l[4])
                    olol.write(str(l))
                print(" > Bye Bye...")
            elif l[1] == "UnPaid":
                print(" > You haven't paid...")
                print(f"Price = {l[7]}")
                cc = input(" > What is your credit card NUmber ? \n > ")
                with open("CC", "a") as ifu:
                    ifu.write(cc)
                    ifu.write("\n")
                with open("Rent Stocks", "w+") as olol:
                    o = olol.read()
                    l = int(o) + int(l[4])
                    olol.write(str(l))
                print(" > Bye Bye...")
# The end of the program
