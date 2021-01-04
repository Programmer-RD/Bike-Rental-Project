from BRKF_R import RAB, RABR
import BRKF_S
import BRKF_I
import Email
import BRKF_B
import CC


def start():
    print("""
     > B = Buy a Bike
     > R = Rent a bIKE
     > I = Bike Instruments
     > P = Problem
     > H = Help     
    """)
    choice = input(" > What is your choice ? \n > ").upper()
    if choice == "B":
        how_many_bike = input(" > How many bikes do you want to buy ? \n > ")
        price = input(" > What is the maximum mount that you can pay ? \n > ")
        lo = BRKF_B.BAB(how_many_bikes=how_many_bike,price_range=price)
        lo.check_stock()
        lo.prices()
        print(CC)
        exit()
        quit()
    elif choice == "R":
        print("""
         > R = Rent a Bike
         > M = Return a Bike
        """)
        what_is_the_choice = input(" > What is your choice ? \n > ").upper()
        if what_is_the_choice == "R":
            id = input(" > what is the id ? \n > ")
            print(" > NOTE : YOU SHOULD REMEMBER THE ABOVE ID TO RETURN YOUR BIKE ! ")
            name = input(" > What is your name ? \n > ")
            bikes = input(' > How many bikes do you want to rent ? \n > ')
            time_type = input(" > What is the time type (H = Hours | D = Day | W = Week) ").upper()
            info = RAB(id=id, name=name, how_many_bikes=bikes, time_type=time_type)
            info.checking_stock()
            info.price()
            print(CC)
            quit()
            exit()
        elif what_is_the_choice == "M":
            id = input(" > What is the id that you gave when you rented the bike ? \n > ")
            r = RABR(id=id)
            r.return_bikes()
            print(CC)
            quit()
            exit()
    elif choice == "I":
        print(BRKF_I)
        print(CC)
        quit()
        exit()
    elif choice == "P":
        name = input(" > What is your name ? \n > ")
        tele = input(" > What is your telephone number ? \n > ")
        what = input(" > What is the problem ? \n > ")
        print(" > If you want to talk call : 0718024596. \n > Email : ranugagamage@gmail.com")
        Email.m(sub="A Problem", bod=what + name + tele)
        print(" > Complain Successful Send...")
        print(" > You will receive a call soon.. \n > THank you....")
        print(CC)
        quit()
        exit()
    elif choice == "H":
        with open("Help", "r") as help:
            print(help.read())
        quit_or_start = input(
            " > Do you want to quit or want to choice an option (Q = quit | L = New option) ? \n > ").upper()
        if quit_or_start == "L":
            start()
        elif quit_or_start == "Q":
            quit()
            exit()
    elif choice == "S":
        print(BRKF_S)
        quit()
        exit()
    else:
        print(" > ! INVALID CHOICE ! < ")
        start()
