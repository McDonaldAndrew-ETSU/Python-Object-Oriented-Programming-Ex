import datetime, math
# Approximate nitrous shot to horsepower(hp) ratio is 1:1.
# Approximate parasitic loss from superchargers is 12% of hp
# Approximate gain of 4% of hp and torque boost per 1 boost psi 
# Twincharger has both super and turbo. The effects of both are combined.
class Car:
    def __init__(self, make, model, year, weight, hp_stock, tq_stock, power_opt, n2o_shot, b_psi):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__weight = weight
        self.__hp_stock = hp_stock
        self.__tq_stock = tq_stock
        self.__power_opt = power_opt
        self.__n2o_shot = n2o_shot
        self.__b_psi = b_psi
        self.__horsepower = self.max_power(hp_stock)
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_weight(self):
        return self.__weight
    def get_hp_stock(self):
        return self.__hp_stock
    def get_tq_stock(self):
        return self.__tq_stock
    def get_power_opt(self):
        return self.__power_opt
    def set_power_opt(self, new_opt):
        self.__power_opt = new_opt
    def get_n2o_shot(self):
        return self.__n2o_shot
    def set_n2o_shot(self, new_n20):
        self.__n2o_shot = new_n20
    def get_b_psi(self):
        return self.__b_psi
    def set_b_psi(self, new_b_psi):
        self.__b_psi = new_b_psi
    def get_horsepower(self):
        return self.__horsepower
    
    def max_power(self, hp_or_tq):
        power_factor = self.get_b_psi() * .04
        gain = hp_or_tq * power_factor
        loss = hp_or_tq * 0.12

        if self.get_power_opt() == 'super':
            force = (hp_or_tq + gain) - loss
        elif self.get_power_opt() == 'turbo' or 'twin':
            force = hp_or_tq + gain
        else: 
            force = hp_or_tq

        if self.get_n2o_shot() > 0:
            force = force + self.get_n2o_shot()

        return force    


class Racer:
    def __init__(self, name, age, five_speed_shifting, drifting, passing, cornering, car):
        self.__name = name
        self.__age = age
        self.__five_speed_shifting = five_speed_shifting
        self.__drifting = drifting
        self.__passing = passing
        self.__cornering = cornering
        self.__car = car
        self.__winner = False
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_five_speed_shifting(self):
        return self.__five_speed_shifting
    def get_drifting(self): 
        return self.__drifting
    def get_passing(self):
        return self.__passing
    def get_cornering(self):
        return self.__cornering
    def get_car(self):
        return self.__car
    # Add setter in near future
    def get_winner(self): 
        return self.__winner
    def set_winner(self, new_winner):
        self.__winner = new_winner


class Race:
    def __init__(self, title, date, racer_list, duration):
        self.__title = title
        self.__date = date
        self.__racer_list = racer_list
        self.__duration = duration
        self.__race_winner = self.declare_winner()
    def get_title(self):
        return self.__title
    def get_date(self):
        return self.__date
    def get_racer_list(self):
        return self.__racer_list
    def get_duration(self):
        return self.__duration
    def get_race_winner(self):
        return self.__race_winner

    def declare_winner(self):
        racers = []
        accelerations = [] # acceleration = SQRT(HP∗745.6992/(2∗mass∗time))
        for racer in self.get_racer_list():
            racers.append(racer)
            acceleration = math.sqrt((racer.get_car().get_horsepower() * 745.6992)/(2 * racer.get_car().get_weight() * self.get_duration()))
            accelerations.append(acceleration)
        
        winning_acceleration = max(accelerations)
        index_of_winning_acceleration = accelerations.index(winning_acceleration)

        winning_racer = racers[index_of_winning_acceleration]
        winning_racer.set_winner(True)
        return winning_racer.get_name()



car_one = Car('Pontiac', 'Catalina', 1966, 4000, 330.0, 400.0, None, 50, 0)
car_two = Car('Plymouth', 'Road Runner', 1969, 3800, 400, 425, None, 50, 0)

racer_one = Racer('Dom Torretta', '28', 10, 7, 9, 8, car_one)
racer_two = Racer('Paul Walker', '26', 9, 7, 10, 10, car_two)

racer_list = [racer_one, racer_two]


def generateRacers(racer):
    print(
        f"\n___________________________________________________________________________\n" +
        f"| Name: {racer.get_name()}\tAge: {racer.get_age()} | Car of Choice:\n" +
        f"| Stats:                        |\t{racer.get_car().get_year()} {racer.get_car().get_make()} {racer.get_car().get_model()}\n" +
        f"| ******                        |\t  Horsepower: {racer.get_car().get_horsepower()}\n" +
        f"|\t5 Speed Shifting: {racer.get_five_speed_shifting()}/10 |\t Forced Induction Charger: {racer.get_car().get_power_opt()}\n" +
        f"|\tDrifting: {racer.get_drifting()}/10         |\n" +
        f"|\tPassing: {racer.get_passing()}/10          |\n" +
        f"|\tCornering: {racer.get_cornering()}/10        | Winner?: {racer.get_winner()}\n" +
        f"****************************************************************************\n" 
    )


for racer in racer_list:
    generateRacers(racer)

race_one = Race('Pink Slip Showdown', datetime.datetime(2004, 6, 24, 10, 24), racer_list, 15.0)

for racer in racer_list:
    generateRacers(racer)

print(f"On {race_one.get_date()}, {race_one.get_race_winner()} was the winner of the {race_one.get_title()}!")