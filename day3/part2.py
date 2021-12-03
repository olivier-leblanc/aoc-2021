
def filter_list_on_index(input_list, index, filter_value):
    """Filtre la liste de binaires selon la position donnée (index) et la valeur

    ex: [00111, 00101, 01000], 2, 1
    On va garder seulement les entrées ayant 1 a la position 2 donc:
    [00111, 00101]
    """
    new_list = []
    for x in input_list:
        if int(x[index]) == int(filter_value):
            new_list.append(x)

    return new_list

def main(input_file):

    BITS_PER_LINE = 12
    
    with open(input_file, "r") as f:
        bin_list = f.readlines()

    oxygen_list = bin_list
    co2_list = bin_list

    for x in range(BITS_PER_LINE):

        # Oxygen = most common
        # co2 = least
        if len(oxygen_list) > 1:
            m = 1 if sum([item[x] == "1" for item in oxygen_list]) >= sum([item[x] == "0" for item in oxygen_list]) else 0
            oxygen_list = filter_list_on_index(oxygen_list, x, m)

        if len(co2_list) > 1:
            least = 0 if sum([item[x] == "0" for item in co2_list]) <= sum([item[x] == "1" for item in co2_list]) else 1
            co2_list = filter_list_on_index(co2_list, x, least)


    life_support = int(oxygen_list[0], 2) * int(co2_list[0], 2)

    print(f"Power of both: {life_support}")

if __name__ == "__main__":
    main("3.input")