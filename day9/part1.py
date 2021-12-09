def get_adjacent_points(array, x, y):

    points = []
    if array.get(x-1, None):
            points.append(array[x-1][y])

    if array.get(x+1, None):
            points.append(array[x+1][y])

    if array.get(y-1, None):
            points.append(array[x][y-1])

    if array.get(y+1, None):
            points.append(array[x][y+1])

    return points

def is_low_point(target, adj_points):
    return all([target < x for x in adj_points])

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
    for i in floor_map.keys():
        for j in floor_map[i].keys():
            adj = get_adjacent_points(floor_map, i, j)
            if is_low_point(floor_map[i][j], adj):
                print(f"lp<{i},{j}>")
                risk_level += floor_map[i][j]+1


    print("Total risk level")
    print(risk_level)

if __name__ == "__main__":
    main("test.input")