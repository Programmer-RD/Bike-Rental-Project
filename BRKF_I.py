print(" > Choices : ")
print("""
 > H = Helmet
 > L = Lubricant
 > P = Pump
 > G = Goggles
 > C = Glasses
 > BB = Bike Bag
 > PK = Patch Kit
 > ST = Spare Tube
 > MT = Minimum Tools
 > CS = Cycling Shoes
 > CG = Cycling Gloves
 > CJ = Cycling Jacket
 > LL = Lock
 > TPG = Tire Pressure Gauge
 > WBC = Water Bottle and Cage
""")
choice = input(" > What is your choice ? \n > ").upper()
if choice == "H":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm["H"]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "L":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("L")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "P":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("P")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "G":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("G")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "C":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("C")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "BB":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("BB")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "PK":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("PK")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "ST":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("ST")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "MT":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("MT")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "CS":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("CS")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "CG":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("CG")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "CJ":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("CJ")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "LL":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("LL")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "TPG":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r") as ip:
        lm = ip.read()
        l = lm[int("TPG")]
        print(f" > Price : {int(l)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
elif choice == "WBC":
    how_many = input(" > How many do you want ? \n > ")
    with open("instruments prices", "r+") as ip:
        lm = ip.read()
        l = lm[int(str("WBC"))]
        print(f" > Price : {int(l) * int(how_many)} ")
    with open("Stocks", "r+") as lol:
        l = lol.read()
        o = l - how_many
        lol.write(o)
    cc = input(" > What is your credit card no : ? \n > ")
    with open("CC", "a+") as c:
        c.write(cc)
        c.write("\n")
    print(" > Your bicycle equipment will be delivered in 5 days...")
with open("CC")