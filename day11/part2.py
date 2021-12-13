class Octopus:

    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = int(val)
        self.flashed = False


def get_adj_octopus(map, x, y):
    """On retourne les octopus a l'entour de celui a la valeur x,y.
    Si on est out of bounds, on met None dans la liste et on va gérer après
    """
    octopus = []

    if map.get(y - 1, None):
        octopus.append(map[y - 1].get(x, None))
        octopus.append(map[y - 1].get(x - 1, None))
        octopus.append(map[y - 1].get(x + 1, None))

    if map.get(y + 1, None):
        octopus.append(map[y + 1].get(x, None))
        octopus.append(map[y + 1].get(x - 1, None))
        octopus.append(map[y + 1].get(x + 1, None))

    octopus.append(map[y].get(x + 1, None))
    octopus.append(map[y].get(x - 1, None))

    return octopus

def handle_octopus_step(map, octopus, increase=True):
    """A chaque pas on:
    - Augmente la valeur de 1
    - Si on est en haut de 9 on flash et on augmente les octopus a l'entour
    - On va gérer leur flash a la fin
    """
    flashes = 0
    if octopus is not None:
        if increase:
            octopus.val += 1
        if octopus.val > 9 and not octopus.flashed:
            flashes += 1
            
            octopus.flashed = True

            for adj_oct in get_adj_octopus(map, octopus.x, octopus.y):

                flashes +=  handle_octopus_step(map, adj_oct)

    return flashes
def make_step(map):
    """On traite un seul pas
    """
    flashes = 0
    for y in map:
        for x in map[y]:
            flashes += handle_octopus_step(map, map[y][x])

    return flashes

def post_step(map):
    """Un coup que tout les flash "natuels" on été gérés,
    On repasse au travers les octopus pour faire flasher ceux en haut de 9
    """
    # Pour le part 2 faut tracker quand les 100 flash en même temps
    total_flashed = 0
    for y in map:
        for x in map[y]:
            if map[y][x].val > 9:
                total_flashed += 1
                map[y][x].val = 0
                map[y][x].flashed = False
    if total_flashed == 100:
        return True
    return False

def main(file_name):
    flashes = 0
    map = {}
    with open(file_name, "r") as f:
        lines = f.readlines()

        for y, l in enumerate(lines):
            for x, o in enumerate(l):
                if o == "\n":
                    continue

                if not map.get(y, None):
                    map[y] = {}

                map[y][x] = Octopus(x, y, o)
        for x in range(9999999):
            flashes += make_step(map)
            if post_step(map) == True:
                print("Step")
                print(x + 1)
                break
            print(flashes)

if __name__ == "__main__":
    main("11.input")
