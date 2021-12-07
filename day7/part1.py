import statistics

def calculate_fuel_for_target(list, target):
    fuel = 0
    for item in list:
        fuel += abs(item - target)

    return fuel

def main(file_name):

    numbers = []
    with open(file_name, "r") as f:
        l = f.read().split(",")

        for x in l:
            numbers.append(int(x))

    # La médiane va nous donner le target dès le début
    # Il y a autant de points au dessus qu'en dessous de la médiane c'est donc
    # forcément le point qui requiert le moins de fioule
    target = statistics.median(numbers)
    best_fuel = calculate_fuel_for_target(numbers, target)

    print(f"Le target '{target}' est meilleur {best_fuel}")

if __name__ == "__main__":
    main("7.input")