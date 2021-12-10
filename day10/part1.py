OPENING_CHARS = ["[", "{", "(", "<"]
CLOSING_CHARS = ["]", "}", ")", ">"]
POINTS = [57, 1197, 3, 25137]

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
                return POINTS[CLOSING_CHARS.index(c)]
    print("La ligne est ok")
    return 0

def main(file_name):

    with open(file_name, "r") as f:
        lines = f.readlines()

    total_score = 0 
    for line in lines:
        total_score += parse_line(line)

    print("Total Score")
    print(total_score)

if __name__ == "__main__":
    main("10.input")