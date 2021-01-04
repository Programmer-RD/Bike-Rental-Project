from datetime import time


class Bike_Rental:

    def __init__(self, how_much_time, how_many_bike, how_many_kid, how_many_people, age_adult, age_kid, money_type):
        self.how_much_time = how_much_time
        self.how_many_bike = how_many_bike
        self.how_many_kids = how_many_kid
        self.how_many_people = how_many_people
        self.age_a = age_adult
        self.age_k = age_kid
        self.money_type = money_type


class money(Bike_Rental):
    def how_much_cost_calculations_Adults(self):
        global z, k
        print(" > Per Hour is Rs 500 ")
        # CALCULATION
        if int(self.how_much_time) > 500:
            k = int(self.how_much_time) * 500
        elif self.how_much_time < 500:
            k = int(self.how_much_time) * 500
        Total_Per_Person = f" > Per Person = {k} {self.money_type} (Adults) "
        if self.how_many_kids == 0:
            pass
        else:
            print(Total_Per_Person)
        if k < int(self.how_many_people):
            z = int(self.how_many_people) * k
        elif k > int(self.how_many_people):
            z = k * int(self.how_many_people)
        Total_Per_All = f" > For Every one = {self.money_type} {z} (Adults) "
        if self.how_many_people == 0:
            pass
        else:
            print(Total_Per_All)

    def how_much_cost_calculations_Kids(self):
        global z, k, x, l
        print(" > Per Hour is Rs 250 ")
        # CALCULATION
        if int(self.how_much_time) > 250:
            x = int(self.how_much_time) * 250
        elif self.how_much_time < 250:
            x = int(self.how_much_time) * 250
        total_Per_Person = f" > Per Person = {x} {self.money_type} (Kids) "
        if self.how_many_kids == 0:
            pass
        else:
            print(total_Per_Person)
        if x < int(self.how_many_people):
            l = int(self.how_many_people) * x
        elif x > int(self.how_many_people):
            l = x * int(self.how_many_people)
        total_Per_All = f" > For Every one = {self.money_type} {l} (kids) "
        if self.how_many_kids == 0:
            pass
        else:
            print(total_Per_All)


z = money(how_much_time=int(56), how_many_bike=int(5), how_many_kid=int(5),
          how_many_people=int(6)
          , age_adult=int(56), age_kid=int(11),
          money_type="$")
z.how_much_cost_calculations_Adults()
z.how_much_cost_calculations_Kids()
#########
