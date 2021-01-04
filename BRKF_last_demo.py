# The start of the program
import pickle
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


class BAB(object):
    def __init__(self, how_many_bikes, colour, price_range, type):

        self.bikes = int(how_many_bikes)
        self.color = colour
        self.price = int(price_range)
        self.type = type
        lk = open("Stocks", "rb")
        self.stock = lk.read()
        lm = open("Prediction", "rb")
        self.prediction = lm.read()

    def new_bikes(self, new_mamount_of_bikes):
        self.bikes = new_mamount_of_bikes

    def new_color(self, new_color):
        self.color = new_color

    def new_price(self, new_price):
        self.price = new_price

    def new_type(self, new_type):
        self.type = new_type

    def check_stock(self):
        if str(self.stock) > str(self.bikes):
            with open("White Stocks", "w") as rdd:
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
                    bg = BAB(how_many_bikes=self.bikes, colour=self.color, price_range=self.price,
                             type=self.type)
                    bg.new_bikes(new_mamount_of_bikes=new_amount_of_bikes)
                    if self.color == "White" or self.color == "white":
                        with open("White Stocks", "w") as rdd:
                            if int(self.stock) < self.bikes:
                                self.stock = int(self.stock) - int(new_amount_of_bikes)
                            else:
                                self.stock = int(new_amount_of_bikes) - int(self.stock)
                    elif self.color == "Black" or self.color == "black":
                        with open("Black Stocks", "w") as rdd:
                            if int(self.stock) < self.bikes:
                                self.stock = int(self.stock) - int(new_amount_of_bikes)
                            else:
                                self.stock = int(new_amount_of_bikes) - int(self.stock)
                    elif self.color == "Yellow" or self.color == "yellow":
                        with open("Yellow Stocks", "w") as rdd:
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
                    " > Thank you.. \n > Sorry that we dont have any stocks.. \n > Please try agin later... \n > "
                    "Hope you understand... \n > Thank you... \n > Bye Bye....")
                # AAUAAuGATAGuyTAYAATIAHTAYLAY

    def price(self):
        with open("Prices", "rb") as klkl:
            lm = pickle.load(klkl)
        if lm["Prices"]["Low"] < self.price and lm["Prices"]["Medium"] < self.price and lm["Prices"][
            "High"] < self.price:
            print(lm["Prices"]["Low"])
            print(lm["Prices"]["Medium"])
            print(lm["Prices"]["High"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            if l == lm["Prices"]["Low"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    credict_card = int(input(" > Please enter your credit card... \n > "))
            elif l == lm["Prices"]["Medium"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    credict_card = int(input(" > Please enter your credit card... \n > "))
            elif l == lm["Prices"]["High"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    credict_card = int(input(" > Please enter your credit card... \n > "))
            print(" > Your bike will be delivered in 5 days")
            print(" > Thank you sir... \n > Bye Bye...")
            exit()
            quit()
        elif lm["Prices"]["Low"] < self.price and lm["Prices"]["Medium"] < self.price:
            print(lm["Prices"]["Low"])
            print(lm["Prices"]["Medium"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            if l == lm["Prices"]["Low"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    credict_card = int(input(" > Please enter your credit card... \n > "))
            elif l == lm["Prices"]["Medium"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    credict_card = int(input(" > Please enter your credit card... \n > "))
            print(" > Your bike will be delivered in 5 days")
            print(" > Thank you sir... \n > Bye Bye...")
            exit()
            quit()
        elif lm["Prices"]["Low"] < self.price and lm["Prices"]["High"] < self.price:
            print(lm["Prices"]["Low"])
            print(lm["Prices"]["High"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            if l == lm["Prices"]["Low"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    credict_card = int(input(" > Please enter your credit card... \n > "))
            elif l == lm["Prices"]["High"]:
                when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                if when_pay == "On delivery" or when_pay == "on delivery":
                    print(" > Ok sir please pay on delivery....")
                elif when_pay == "Online" or "online":
                    when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
                    if when_pay == "On delivery" or when_pay == "on delivery":
                        print(" > Ok sir please pay on delivery....")
                    elif when_pay == "Online" or "online":
                        credict_card = int(input(" > Please enter your credit card... \n > "))
            print(" > Your bike will be delivered in 5 days")
            print(" > Thank you sir... \n > Bye Bye...")
            exit()
            quit()
        elif lm["Prices"]["High"] < self.price and lm["Prices"]["Medium"] < self.price:
            print(lm["Prices"]["High"])
            print(lm["Prices"]["Medium"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            if l == lm["Prices"]["High"]:
                print(lm["Prices"]["High"])
                l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
                print(" > Your bike will be delivered in 5 days")
                print(" > Thank you sir... \n > Bye Bye...")
                exit()
                quit()
            elif l == lm["Prices"]["Medium"]:
                print(lm["Prices"]["Medium"])
                l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
                print(" > Your bike will be delivered in 5 days")
                print(" > Thank you sir... \n > Bye Bye...")
                exit()
                quit()
        elif lm["Prices"]["Low"] < self.price:
            print(lm["Prices"]["Low"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            print(" > Your bike will be delivered in 5 days")
            print(" > Thank you sir... \n > Bye Bye...")
            exit()
            quit()
        elif lm["Prices"]["Medium"] < self.price:
            print(lm["Prices"]["Medium"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            print(" > Your bike will be delivered in 5 days")
            print(" > Thank you sir... \n > Bye Bye...")
            exit()
            quit()
        elif lm["Prices"]["High"] < self.price:
            print(lm["Prices"]["High"])
            l = input(" > Which of the above do you wat to buy ? (From the prices above) \n > ")
            print(" > Your bike will be delivered in 5 days")
            print(" > Thank you sir... \n > Bye Bye...")
            exit()
            quit()

    def information(self):
        global credict_card
        name = input(" > What is your name ? \n > ")
        age = int(input(" > How old are you  ?\n > "))
        tele_no = int(input(" > What is your phone number ? \n > "))
        addres = input(" > What is your address ? \n > ")
        id = input(" > What is the id (A secret password that only you know) ? \n > ")
        print(""" > NOTE : 
        YOU SHOULD USE THE ABOVE ID WHEN YOU ARE TAKING THE BIKE ! 
        """)
        when_pay = input(" > When are you going to pay (On deliver or online) ? \n > ")
        if when_pay == "On delivery" or when_pay == "on delivery":
            print(" > Ok sir please pay on delivery....")
        elif when_pay == "Online" or "online":
            credict_card = int(input(" > Please enter your credit card... \n > "))
        with open(f"{id}", "w") as lkl:
            lkl.write(name)
            lkl.write("\n")
            lkl.write(str(age))
            lkl.write("\n")
            lkl.write(str(tele_no))
            lkl.write("\n")
            lkl.write(addres)
            lkl.write("\n")
            lkl.write(when_pay)


class RAB(object):
    def __init__(self, how_many_bikes, how_much_time, id, name):
        self.bikes = how_many_bikes
        self.time = how_much_time
        with open("Rent Stocks", "w+") as lklk:
            self.stock = lklk.read()
        if self.time == "H" or self.time == "h":
            self.time_type = f"Rs {6 * 185.77}"
        elif self.time == "D" or self.time == "d":
            self.time_type = f"Rs {20 * 185.77}"
        elif self.time == "W" or self.time == "w":
            self.time_type = f"Rs {60 * 185.77}"
        self.id = id
        self.name = name

    def new_bikes(self, new_bikes):
        self.bikes = new_bikes

    def new_time(self, new_time):
        self.time = new_time

    def new_id(self, new_id):
        self.id = new_id

    def new_name(self, new_name):
        self.name = new_name

    def stock_check(self):
        if self.stock < self.bikes:
            with open("Rent Stocks", "w") as rdd:
                self.stock = int(self.stock) - int(self.bikes)
                rdd.write(str(self.stock))
            print(" > Stocks are available....")
            print(" > Processing....")
            time.sleep(10)
        else:
            print(f" > We don't have {self.bikes}... \n > But we have {self.stock}...")
            new_value = input(f" > Do you want to buy bikes less than {self.stock} (Y/N) ? \n > ")
            if new_value == "Y" or new_value == "y":
                new_bike = int(input(" > What is the new bike value ? \n > "))
                ol = RAB(how_many_bikes=self.bikes, how_much_time=self.time, id=self.id, name=self.name)
                ol.new_bikes(new_bikes=new_bike)
                with open("Rent Stocks", "w+") as rdd:
                    self.stock = int(self.stock) - int(new_bike)
                    rdd.write(str(self.stock))
                print(" > Stocks are available....")
                print(" > Processing....")
                time.sleep(10)
            elif new_value == "N" or new_value == "n":
                print("> OK then... \n > hHank you for using our program.... \n > Hope you have a nice day.... \n > "
                      "Bye Bye....")
                print(f" > In {round(self.stock)}, there would be stocks available ")
                print(" > Sorry we don't have any stocks... \n > I am sorry... \n > Thank you... \n > Bye Bye...")
                print(" > Hope you understand....")
                quit()
                exit()

    def price_bikes(self):
        if self.time_type == "H" or self.time_type == "h":
            ms = self.time * self.bikes
            when_pay = input(" > Are you going to pay N = now or R = When you are returning ? \n > ").upper()
            if when_pay == "N":
                credit_card = input(" > What is the credit card number  ? \n > ")
                devin = True
                time.sleep(10)
                print(" > Transaction completed....")
                with open(f"{self.id}", "a+") as sll:
                    sll.write(str(ms))
                    sll.write("\n")
                    sll.write(str(devin))
                    sll.write("\n")
                    sll.write(self.name)
                    sll.write("\n")
                    sll.write(str(self.bikes))
                print(" > Ok...")
                print(" > You have successfully rented a bike....")
                print(" > Hope you enjoy it...")
                print(" > Return it in the correct time...")
                print(" > Checking Bikes.....")
                time.sleep(10)
                print(f" > Your bikes number is {random.choices(range(1, 565665))}")
                print(" > Bye Bye....")
            elif when_pay == "R":
                devin = False
                print(" > Ok...")
                print(" > You have successfully rented a bike....")
                print(" > Hope you enjoy it...")
                print(" > Return it in the correct time...")
                print(" > Checking Bikes.....")
                time.sleep(10)
                with open(f"{self.id}", "a+") as sll:
                    sll.write(str(ms))
                    sll.write("\n")
                    sll.write(str(devin))
                    sll.write("\n")
                    sll.write(self.name)
                    sll.write("\n")
                    sll.write(str(self.bikes))
                print(f" > Your bikes number is {random.choices(range(1, 565665))}")
                print(" > Bye Bye....")
        elif self.time_type == "D" or self.time_type == "d":
            ms = self.time * self.bikes
            when_pay = input(" > Are you going to pay N = now or R = When you are returning ? \n > ").upper()
            if when_pay == "N":
                credit_card = input(" > What is the credit card number  ? \n > ")
                devin = True
                time.sleep(10)
                print(" > Transaction completed....")
                with open(f"{self.id}", "a+") as sll:
                    sll.write(str(ms))
                    sll.write("\n")
                    sll.write(str(devin))
                    sll.write("\n")
                    sll.write(self.name)
                    sll.write("\n")
                    sll.write(str(self.bikes))
                print(" > Ok...")
                print(" > You have successfully rented a bike....")
                print(" > Hope you enjoy it...")
                print(" > Return it in the correct time...")
                print(" > Checking Bikes.....")
                time.sleep(10)
                print(f" > Your bikes number is {random.choices(range(1, 565665))}")
                print(" > Bye Bye....")
            elif when_pay == "R":
                devin = False
                print(" > Ok...")
                print(" > You have successfully rented a bike....")
                print(" > Hope you enjoy it...")
                print(" > Return it in the correct time...")
                print(" > Checking Bikes.....")
                time.sleep(10)
                with open(f"{self.id}", "a+") as sll:
                    sll.write(str(ms))
                    sll.write("\n")
                    sll.write(str(devin))
                    sll.write("\n")
                    sll.write(self.name)
                    sll.write("\n")
                    sll.write(str(self.bikes))
                print(f" > Your bikes number is {random.choices(range(1, 565665))}")
                print(" > Bye Bye....")

        elif self.time_type == "W" or self.time_type == "w":
            ms = self.time * self.bikes
            when_pay = input(" > Are you going to pay N = now or R = When you are returning ? \n > ").upper()
            if when_pay == "N":
                credit_card = input(" > What is the credit card number  ? \n > ")
                devin = True
                time.sleep(10)
                print(" > Transaction completed....")
                with open(f"{self.id}", "a+") as sll:
                    sll.write(str(ms))
                    sll.write("\n")
                    sll.write(str(devin))
                    sll.write("\n")
                    sll.write(self.name)
                    sll.write("\n")
                    sll.write(str(self.bikes))
                print(" > Ok...")
                print(" > You have successfully rented a bike....")
                print(" > Hope you enjoy it...")
                print(" > Return it in the correct time...")
                print(" > Checking Bikes.....")
                time.sleep(10)
                print(f" > Your bikes number is {random.choices(range(1, 565665))}")
                print(" > Bye Bye....")
            elif when_pay == "R":
                devin = False
                print(" > Ok...")
                print(" > You have successfully rented a bike....")
                print(" > Hope you enjoy it...")
                print(" > Return it in the correct time...")
                print(" > Checking Bikes.....")
                time.sleep(10)
                with open(f"{self.id}", "a+") as sll:
                    sll.write(str(ms))  # 1
                    sll.write("\n")  # 2
                    sll.write(str(devin))  # 3
                    sll.write("\n")  # 4
                    sll.write(self.name)  # 5
                    sll.write("\n")  # 6
                    sll.write(str(self.bikes))  # 7
                print(f" > Your bikes number is {random.choices(range(1, 565665))}")
                print(" > Bye Bye....")

    def return_bikes(self):
        id = input(" > What is the id that you entered when you rented the bike. \n > ")
        file_variable = open(id, 'r+')
        all_lines_variable = file_variable.readlines()
        bike = all_lines_variable[- 1]
        with open("Rent Stocks", "w+") as bg:
            lmsoo = bg.read()
            oo = lmsoo + bike
            bg.write(str(oo))
        paid_or_not = all_lines_variable[1]
        if paid_or_not == "True" or paid_or_not == True:
            print(" > Thank you for bring back the bike.... \n > Hope you enjoyed it... \n > Bye Bye....")
        elif paid_or_not == "False" or paid_or_not == False:
            print(f" > You have to pay {all_lines_variable[0]}....")
            which_way = input(" > Are you going to pay cash or credit card ? \n > ").upper()
            if which_way == "CASH":
                print("> Ok... \n > I have told the cashier your name and the information he will come soon... \n > "
                      "Wait.. \n > Bye Bye... \n Hope you enjoyed the bike...")
                quit()
                exit()
            elif which_way == "CREDIT CARD":
                credit_card = input(" > What is the credit card number ? \n > ")
                print(" > Processing....")
                time.sleep(10)
                print(" > Transaction completed...")
                quit()
                exit()


class I(object):
    pass


def start():
    global x
    print(" > | WELCOME TO DSI BIKE | < ")
    print(" > Choices : ")
    choices = input("""
     > B = Buy a Bike.
     > R = Rent a Bike.
     > P = Problem.
     > I = Bike instruments.
     > Q = quit.
     > Enter your Choice :  
     > """)
    if choices == "B" or choices == "b":
        how_many_bike = input(" > How many bikes do you want to buy ? \n > ")
        colour = input(" > What is the color of the bike ? \n > ")
        price = input(" > What is the maximum amount of monney that you can pay ? \n > ")
        type_of_the_bike = input(" > What is the type of the bike ? \n > ")
        ll = BAB(how_many_bikes=how_many_bike, colour=colour, price_range=price, type=type_of_the_bike)
        print(f"""
         > Bikes = {how_many_bike}
         > Color = {colour}
         > Price = {price}
         > Type = {type_of_the_bike}
        """)
        true = input(" > Are the above information correct (Y/N) ? \n > ")
        if true == "Y" or true == "y":
            ll.check_stock()
            var = ll.price
            ll.information()
            print("> Thank you.. \n Your bike will be delivered to you in 5 days... \n for more information call : "
                  "0718732829 ")
        else:
            which_is_wrong = input(" > What is the problem ? \n > ")
            if which_is_wrong == "Bikes" or which_is_wrong == "bikes":
                new_bikes = input(" > What is the new bike value ? \n > ")
                ll.new_bikes(new_mamount_of_bikes=new_bikes)
            elif which_is_wrong == "Colour" or which_is_wrong == "colour":
                new_color = input(" > What is new color ? \n > ")
                ll.new_color(new_color=new_color)
            elif which_is_wrong == "Price" or which_is_wrong == "price":
                new_price = input(" > What is the new price ? \n > ")
                ll.new_price(new_price=new_price)
            elif which_is_wrong == "Type" or which_is_wrong == "type":
                new_type = input(" > What is the new type ? \n > ")
                ll.new_type(new_type=new_type)
            else:
                print(" > Invalid Choice ! ")
                start()
    elif choices == "P" or choices == "p":
        what = input(" > What is the problem ? \n > ")
        print(" > If you want to call : 0718024596 ")
        print(" > Email : ranugagamage@gmail.com ")

        def send_mail(Subject=what, mes=what):
            msg = MIMEMultipart()
            msg['From'] = "go2testcode@gmail.com@gmail.com"
            msg['To'] = "ranugagamage@gmaill.com"
            msg['subject'] = Subject
            msg.attach(MIMEText(mes, 'plain'))

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com')
                server.ehlo()
                server.login("go2testcode@gmail.com", "Ranuga2008")
                try:
                    server.sendmail("go2testcode@gmail.com", "ranugagamage@gmaill.com", msg.as_string())
                except:
                    server.sendmail("go2testcode@gmail.com", "ranugagamage@gmaill.com", msg.as_bytes())
                server.close()
                return True
            except Exception as e:
                print(" > Something went wrong.... \n > The error is " + str(e))
                return False
    elif choices == "R" or choices == "r":
        time_type = input(" > What is the time type (H = Hour | D = Day | W = Week) ? \n > ")
        how_much = input(" > How much time do you want to rent the bike (10,5,6,etc...) ? \n > ")
        id = input(" > Enter a id... \n > ")
        email = input(" > What is your email adress ? \n > ")
        msg = MIMEMultipart()
        msg['From'] = "go2testcode@gmail.com@gmail.com"
        msg['To'] = email
        msg['subject'] = "This is the bike rental code.... \n Rember this ! "
        msg.attach(MIMEText(id))
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.ehlo()
            server.login("go2testcode@gmail.com", "Ranuga2008")
            try:
                server.sendmail("go2testcode@gmail.com", "ranugagamage@gmail.com", msg.as_string())
            except:
                server.sendmail("go2testcode@gmail.com", "ranugagamage@gmail.com", msg.as_bytes())
            server.close()
        except Exception as e:
            print(e)
        name = input(" > What is your name ? \n > ")
        lms = RAB(how_many_bikes=how_much, how_much_time=time_type, id=id, name=name)
        print(f"""
         > Time Type : {time_type}
         > How Much Time : {how_much}
         > Id : {id}
         > Name : {name} 
        """)
        info = input(" > Is the above information correct (Y/N) ? \n > ")
        if info == "Y" or info == "y":
            print(""
                  " > R = Rent \n"
                  " > L = Return a bike")
            choicess = input(" > What is your choice ? \n > ")
            if choicess == "R" or choicess == "r":
                lms.stock_check()
                lms.price_bikes()
            elif choicess == "L" or choicess == "l":
                lms.return_bikes()
            print(" > Thank you for using our program... \n > Bye Bye ...")
        elif info == "N" or info == "n":
            what = input(" > What is the wrong one (T = Time Type | H = How Much Time | I = id | N = Name) ? \n > ")
            if what == "T" or what == "t":
                new_time_type = input(" > What is the new Time Type ? \n > ")
                lms.new_time(new_time=new_time_type)
            elif what == "H" or what == "h":
                new_much = input(" > What is the new time that you want to rent the bike ? \n > ")
                lms.new_bikes(new_bikes=new_much)
            elif what == "I" or what == "i":
                new_id = input(" > What is the new id ? \n > ")
                lms.new_id(new_id=new_id)
            elif what == "N" or what == "n":
                new_name = input(" > What is the new name ? \n > ")
                lms.new_name(new_name=new_name)
    elif choices == "q" or choices == "Q":
        print(" > Thank you for using our program... \n > ...Bye Bye... < ")
        quit()
        exit()
    elif choices == "The Secret password":
        id = input(" > What is your id ? \n > ")
        with open("id.pickle", "rb") as klkl:
            ll = pickle.load(klkl)
            if ll[id] is not None:
                name = input(" > What is your name ? \n > ")
                with open("Secret", "a") as llllll:
                    llllll.write(name)
                with open("Yellow Stocks", "r") as slm:
                    l = slm.read()
                with open("Black Stocks", "r") as bns:
                    o = bns.read()
                with open("White Stocks", "r") as sl:
                    lo = sl.read()
                with open("Stocks", 'r+') as io:
                    ol = int(lo) + int(o) + int(l)
                    io.write(str(ol))
                print("choices : ")
                print("""
                         > S = New Stock
                         > E = Tell the hq that the stocks are almost over 
                         > Q  = quit
                         > N = New employee id and password
                         > P = Predict 
                    """)
                choice = input(" > What is your choice ? \n > ")
                if choice == "S" or choice == "s":
                    new_stock = input(" > Wha is the new stock value ? \n > ")
                    what_color = input(" > What is tyhe color ? \n > ")
                    if what_color == "White" or what_color == "white":
                        with open("White Stocks", "w+") as ka:
                            ka.write(new_stock + ka.read())
                            print(" > Stock updated....")
                    elif what_color == "Black" or what_color == "black":
                        with open("Black Stocks", "w+") as ka:
                            ka.write(new_stock + ka.read())
                            print(" > Stock updated....")
                    elif what_color == "Yellow" or what_color == "yellow":
                        with open("Yellow Stocks", "w+") as ka:
                            ka.write(new_stock + ka.read())
                            print(" > Stock updated....")
                elif choice == "E" or choice == "e":
                    to = input(" > the to persons email adress ? \n > ")
                    msg = MIMEMultipart()
                    msg['From'] = "go2testcode@gmail.com@gmail.com"
                    msg['To'] = "ranugagamage@gmail.com"
                    msg['subject'] = "Need White Stocks ! (Kaduwela) DSI ! "
                    with open("White Stocks", "r") as lms:
                        msg.attach(MIMEText(f"We only have {lms.read()} \n Bring the stocks soon... \n "
                                            f"Thank you.. \n "
                                            f"Your truthful \n {name} ", 'plain'))
                    try:
                        server = smtplib.SMTP_SSL('smtp.gmail.com')
                        server.ehlo()
                        server.login("go2testcode@gmail.com", "Ranuga2008")
                        try:
                            server.sendmail("go2testcode@gmail.com", "ranugagamage@gmail.com", msg.as_string())
                        except:
                            server.sendmail("go2testcode@gmail.com", "ranugagamage@gmail.com", msg.as_bytes())
                        server.close()
                        return True
                    except Exception as e:
                        print(" > Something went wrong.... \n > The error is " + str(e))
                        return False
                elif choice == "P" or choice == "p":
                    wh = input(" > What kind of a day is it (Monday,Tuesday,etc...) ? \n > ")
                    x = {}
                    for i in range(1, 5):
                        day = input(f" > How many bikes came in the {i} {wh} ? \n > ")
                        x[i] = day
                        total_x = int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])
                        with open("Stocks", "r") as kl:
                            p = total_x / 4 / int(kl.read())
                            p = round(p)
                            l = p / 3
                            l = round(l)
                        print(f" > We only have {l} days till the stock is finished")
                elif choice == "N" or choice == "n":
                    id = input(" > What is the id ? \n > ")
                    password = input(" > What is the password ? \n > ")
                    D = open("Name_Email.txt", "a")
                    D.write({id: password})
                    D.close()
                elif choice == "q" or choice == "Q":
                    print(" > ....Bye Bye.... < ")
                    quit()
                    exit()

    else:
        print(" > Wrong Choice ! ")
        start()


start()
# the end of the program
