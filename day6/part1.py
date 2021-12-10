class Fish():

    def __init__(self, timer):
        self.timer = timer

def main(file_name):
    DAYS_TO_SIMULATE = 80
    numbers=[]
    with open(file_name, "r") as f:
        numbers=[Fish(int(x)) for x in f.readline().replace("\n", "").split(",")]

    for _ in range(DAYS_TO_SIMULATE):
        new_fish = []
        for fish in numbers:
            if fish.timer == 0:
                new_fish.append(Fish(8))
                fish.timer = 6
            else:
                fish.timer -= 1
        
        print(f"Après le jour {_}, on a {len(numbers)} fish et {len(new_fish)} nouveau poissons")
        numbers += new_fish

    print(len(numbers))
    
if __name__ == "__main__":

    main("6.input")