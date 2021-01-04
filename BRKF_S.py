import time
import Email

id = input(" > What is your id ? \n > ")
with open("id", "r") as di:
    l = di.read()
    k = l[int(id)]
    name = k[int("Name")]
    if k is not None:
        print(" > ! Access granted ! < ")
        print(" > Choice : ")
        print("""
         > S = New Stock
         > E = Tell the hq that the stocks are almost over 
         > N = New employee id and password
         > P = Predict 
         > Q = quit
        """)
        choice = input(" > What is your choice ? \n > ").upper()
        if choice == "S":
            stocks = input(" > New Stocks amount... \n > ")
            with open("Rent Stocks", "w+") as rs:
                ls = rs.read()
                sl = int(ls) + int(stocks)
                rs.read(sl)
            print(" > Processing...")
            time.sleep(10)
            print(" > Stocks Updated...")
        elif choice == "E":
            sub = input(" > What is the Subject ? \n > ")
            bod = input(" > What is the body ? \n > ")
            Email.m(sub=sub + name, bod=bod + name)
        elif choice == "N":
            id = input(" > What is the id ? \n > ")
            password = input(' > What is the password ? \n > ')
            with open("id", "w+") as ool:
                ool.write(str({id: password}))
            print(" > Id Updated...")
        elif choice == "P":
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
        elif choice == "Q":
            quit()
            exit()
    elif k is None:
        print(" > ! Access denied ! < ")
        quit()
        exit()
