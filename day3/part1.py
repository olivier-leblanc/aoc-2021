
def get_most_and_least_common_bit(input_list, index):
    """On retourne un tuple du bit le plus et le moins commmun 1 ou 0 dans la liste donnée
    pour la position donnée

    ex: [00111, 00101, 01000]
    index = 2
    On va retourner (1, 0) puisqu'il y a deux 1 et un 0 a la position 2 de chaque
    item.
    """
    zeroes = 0
    ones = 0
    for x in input_list:
        if str(x[index]) == "0":
            zeroes += 1
        
        if str(x[index]) == "1":
            ones += 1
         
    if zeroes > ones:
        return 0, 1

    return 1, 0

def main(input_file):

    BITS_PER_LINE = 12
    
    with open(input_file, "r") as f:
        bin_list = f.readlines()
    
    gamma_rate = ""
    epsilon_rate = ""

    for x in range(BITS_PER_LINE):
        most, least = get_most_and_least_common_bit(bin_list, x)

        print(f"MOST:{most} LEAST:{least}")

        gamma_rate += str(most)
        epsilon_rate += str(least)

    
    power = int(gamma_rate, 2) * int(epsilon_rate, 2)

    print(f"Power of sub: {power}")

if __name__ == "__main__":
    main("3.input")