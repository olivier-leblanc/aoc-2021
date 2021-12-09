class Point(object):
    def __init__(self, x, y, val=None):
        self.x = x
        self.y = y
        self.val = val

    def get_val(self, map):
        self.val = map[self.x][self.y]

    # On implémente < et > pour faciliter les comparaisons
    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        if other.val == 9 or self.val == 9:
            return False
        return self.val > other.val

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"<({self.x},{self.y}:{self.val})>"

    def get_adjacent_points(self, map):
        """Retourne une liste des points adjacents
        map: Le dict de dict du floormap
        """

        points = []
        if map[self.y].get(self.x-1, None) is not None:
                p = Point(self.x-1, self.y, map[self.y][self.x-1])
                points.append(p)

        if map[self.y].get(self.x+1, None) is not None:
                p = Point(self.x+1, self.y, map[self.y][self.x+1])
                points.append(p)

        if map.get(self.y-1, None) is not None:
                p = Point(self.x, self.y-1, map[self.y-1][self.x])
                points.append(p)

        if map.get(self.y+1, None) is not None:
                p = Point(self.x, self.y+1, map[self.y+1][self.x])
                points.append(p)

        #print(f"ADJ FOR {self}: {points}")
        return points


def is_low_point(target, adj_points):
    return all([target.val < x.val for x in adj_points])

def get_basin(array, low_point:Point):
    """On cherche le bassin depuis le low point (x, y) donné
    A partir du low point, on doit "remonter" les x et les y jusqu'a temps qu'on
    pogne 9 ou un point plus bas (mais ça ne devrait pas arriver d'après l'énoncé) 
    """
    # Liste de Point object pour faciliter les opérations
    points = [low_point]

    for point in low_point.get_adjacent_points(array):
        if point > low_point:
            # On a un point plus élevé, on l'ajoute a la liste
            if point not in points:
                points.append(point)
                # On recurse!!!!!!!!
                adj_points = get_basin(array, point)
                # Un coup que nous sommes remontés les autres points, on les
                # ajoute au bassin courant
                for p in adj_points:
                    if p not in points:
                        points.append(p)
    
    return points


def main(file_name):
    floor_map={}
    risk_level = 0
    with open(file_name, "r") as f:
        for i, x in enumerate(f.readlines()):
            for j, y in enumerate(x):
                if y == "\n":
                    continue
                if not floor_map.get(int(i), None):
                    floor_map[int(i)] = {}

                floor_map[int(i)][int(j)] = int(y)

    # On doit maintenant trouver les low points
    basins = set()
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            p = Point(x, y, floor_map[y][x])
            adj = p.get_adjacent_points(floor_map)
            if is_low_point(p, adj):
                # Un coup qu'on est dans un low point, on doit trouver la
                # grosseur du bassin
                low_point = p
                print(f"Low Point:{low_point}")
                b = get_basin(floor_map, low_point)
                basins.add((y, x, len(b)))

    biggest_basins = sorted(basins, key=lambda x: x[2], reverse=True)[:3]
    print(biggest_basins)

if __name__ == "__main__":
    main("9.input")
