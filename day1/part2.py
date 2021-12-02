

def main(file_name):
    
    with open(file_name, "r") as f:
        lines = f.readlines()

    increases = 0
    for x in range(len(lines)):

        current_mesurement = get_sliding_measurements(lines, x)
        next_mesurement = get_sliding_measurements(lines, x + 1)

        # Pu assez de data pour continuer on arrête tout
        if next_mesurement is None:
            break

        if current_mesurement < next_mesurement:
            increases += 1
        
    print(f"Number of increases: {increases}")

def get_sliding_measurements(input_list, start_index):
    """Retourne une liste des 3 mesures depuis l'index de début `start_index`
    """
    if len(input_list[start_index:start_index+3]) != 3:
        return None
    return sum(int(x) for x in input_list[start_index:start_index+3])

if __name__ == "__main__":
    main("1.input")