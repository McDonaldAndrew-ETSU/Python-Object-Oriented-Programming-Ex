import fast_and_furious_classes as faf
import datetime


car_one = faf.Car('Pontiac', 'Catalina', 1966, 4000, 330.0, 400.0, None, 50, 0)
car_two = faf.Car('Plymouth', 'Road Runner', 1969, 3800, 400, 425, None, 50, 0)

racer_one = faf.Racer('Dom Torretta', '28', 10, 7, 9, 8, car_one)
racer_two = faf.Racer('Paul Walker', '26', 9, 7, 10, 10, car_two)

racer_list = [racer_one, racer_two]



for racer in racer_list:
    racer.generateRacers()

race_one = faf.Race('Pink Slip Showdown', datetime.datetime(2004, 6, 24, 10, 24), racer_list, 15.0)

for racer in racer_list:
    racer.generateRacers()


print(f"On {race_one.get_date()}, {race_one.get_race_winner()} was the winner of the {race_one.get_title()}!")