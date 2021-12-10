OPENING_CHARS = ["[", "{", "(", "<"]
CLOSING_CHARS = ["]", "}", ")", ">"]
POINTS = [2, 3, 1, 4]

def auto_complete(stack):
    #On complete une ligne avec le stack donné
    line_score = 0

    for c in stack:
        closing_idx = OPENING_CHARS.index(c)

        line_score *= 5
        line_score += POINTS[closing_idx]

    return line_score

def parse_line(line):

    # On passe au travers dla ligne
    # Pour chaque ligne on garde un stack
    # des opening et closing chars. Ca va
    # nous permettre de savoir dans quel ordre
    # on doit fermer les paires

    open_stack = []

    for c in line:
        if c in OPENING_CHARS:
            print("On ajoute '{}' au stack".format(c))
            open_stack.insert(0, c)
            continue

        if c in CLOSING_CHARS:
            # Si on trouve un caractère de fermeture
            # on regarde dans le stack, et on devrait normalement
            # avoir le caractère d'ouverture en premier.
            first_char_in_stack = open_stack.pop(0)
            expected = CLOSING_CHARS[OPENING_CHARS.index(first_char_in_stack)]
            if c == expected:
                print("Ok a date")
            else:
                print("SYNTAX ERROR. GOT {} EXPECTED {}".format(c, expected))
                return 0

    print("La ligne est ok")
    return auto_complete(open_stack)


def main(file_name):

    with open(file_name, "r") as f:
        lines = f.readlines()

    scores = []
    for line in lines:
        line_score = parse_line(line)
        if line_score != 0:
            scores.append(line_score)

    millieu = round(len(scores) / 2)
    print("Score du millieu")
    print(sorted(scores)[int(millieu)])

if __name__ == "__main__":
    main("10.input")