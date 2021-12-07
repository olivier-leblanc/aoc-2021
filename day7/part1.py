
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

    min_number = min(numbers)
    max_number = max(numbers)
    best_fuel = calculate_fuel_for_target(numbers, min_number)
    for possible_target in range(max_number + 1):
        temp_fuel = calculate_fuel_for_target(numbers, possible_target)

        if temp_fuel < best_fuel:
            print(f"Le target '{possible_target}' est meilleur {temp_fuel}<{best_fuel}")
            best_fuel = temp_fuel

    print(best_fuel)

if __name__ == "__main__":
    main("7.input")