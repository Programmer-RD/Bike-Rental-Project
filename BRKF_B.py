import time


class BAB(object):
    def __init__(self, how_many_bikes, price_range):

        self.bikes = int(how_many_bikes)
        self.price = int(price_range)
        lk = open("Stocks", "rb")
        self.stock = lk.read()

    def new_bikes(self, new_amount_of_bikes):
        self.bikes = new_amount_of_bikes

    def new_price(self, new_price):
        self.price = new_price

    def check_stock(self):
        if str(self.stock) > str(self.bikes):
            with open("Stocks", "w") as rdd:
                if int(self.stock) > self.bikes:
                    self.stock = int(self.stock) - int(self.bikes)
                else:
                    self.stock = int(self.bikes) - int(self.stock)
                rdd.write(str(self.stock))
            print(" > Processing......")
            time.sleep(10)
            print(" > Thank you for using our program... \n > Have a nice day sir... \n > Thank you....")
        else:
            if str(self.stock) > str(0):
                print(f" > We only have {self.stock} only... \n > But you ordered {self.bikes}...")
                change_amount = input(" > Do you want to get less bikes ? (Y/N) \n > ")
                if change_amount == "Y" or change_amount == "y":
                    new_amount_of_bikes = int(input(" > What is the new amount of bikes ? \n > "))
                    bg = BAB(how_many_bikes=self.bikes, price_range=self.price)
                    bg.new_bikes(new_amount_of_bikes=new_amount_of_bikes)
                    with open("Stocks", "w") as rdd:
                        if int(self.stock) < self.bikes:
                            self.stock = int(self.stock) - int(new_amount_of_bikes)
                        else:
                            self.stock = int(new_amount_of_bikes) - int(self.stock)
                    print(" > Processing......")
                    time.sleep(10)
                    with open("White Stocks", "w") as rdd:
                        self.stock = int(self.stock) - int(self.bikes)
                        rdd.write(str(self.stock))
                else:
                    print(" > Thank you for using our program... \n > Have a nice day sir... \n > Thank you....")
                    quit()
                    exit()
            else:
                print(
                    " > Thank you.. \n > Sorry that we dont have any stocks.. \n > Please try again later... \n > "
                    "Hope you understand... \n > Thank you... \n > Bye Bye....")

    def prices(self):
        with open("bike rpice", "r") as bp:
            b = bp.read()
            p = b * self.bikes
        print(f" > THe price is : {p} ")
        when_pay = input(" > When are you going to pay (N = Now | D = On Delivery ) ? \n > ").upper()
        if when_pay == "N":
            cc = input(" > What is the credit card number  ? \n > ")
            with open("CC", "w") as cs:
                cs.write(str(cc))
                cs.write("\n")
            print(" > The bike will arrive in 5 days...")
            print(" > For more information call 0718024596..")
            quit()
            exit()
        elif when_pay == "D":
            print(" > The bike will arrive in 5 days...")
            print(" > For more information call 0718024596..")
            quit()
            exit()
