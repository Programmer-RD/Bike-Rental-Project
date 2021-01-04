with open("Tests", "w") as lo:
    lo.write(str({"P": 56, "R": 566666666666666}))
with open("Tests", "w+") as lo:
    o = lo.read()
    print(o)
    o = dict(o)
    print(o)
    los = o["P"] = 85421
    lo = o["R"] = 21
    print(o)
