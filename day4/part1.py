import re

class BingoCardNumber(object):
    def __init__(self, number):
        self.number = int(number)
        self.punched = False

    def punch(self):
        self.punched = True


class BingoCard(object):
    
    def __init__(self):
        self.lines = []

    def add_line(self, line_str):
        """Ajoute la ligne donnée à la carte de bingo.
        Ex: 45 74 77 88  5\n
        """
        new_line = []
        for i in line_str.split(" "):
            # Desfois on a 2 espaces pour le formatting.
            if i != "":
                number = BingoCardNumber(int(i))
                new_line.append(number)

        self.lines.append(new_line)

    @property
    def has_bingo(self):
        return self.validate_bingo_cols() or self.validate_bingo_lines()

    def get_number(self, number):
        """On retourne le numéro s'il existe dans la carte
        """

        for line in self.lines:
            for j in line:
                if j.number == int(number):
                    return j
        
        return None

    def handle_number(self, number):
        """On punch le numéro donné sur la carte
        """

        number_in_card = self.get_number(number)
        if number_in_card:
            number_in_card.punch()


    def validate_bingo_lines(self):
        for i in self.lines:
            if sum([1 if j.punched == True else 0 for j in i]) == 5:
                return True

        return False

    def validate_bingo_cols(self):
    
        for i in range(5):
            punched_in_col = 0
            for j in self.lines:
                if j[i].punched is True:
                    punched_in_col += 1

            if punched_in_col == 5:
                return True

        return False

    def get_score(self):
        total = 0
        for line in self.lines:
            for n in line:
                if not n.punched:
                    total += n.number

        return total


def main(file_name):
    
    boules = []
    cards = []
    with open(file_name, "r") as f:
        # Les boules sont dans la première ligne
        boules = f.readline().split(",")
        # On skip la ligne suivante qui est vide
        next(f)

        # Chaque carte est les 5 lignes suivantes
        current_card = BingoCard()
        for line in f:

            if line == "\n":
                # La carte est remplie donc on l'ajoute a la liste des cartes
                cards.append(current_card)

                # On crée une nouvelle carte
                current_card = BingoCard()

            else:
                current_card.add_line(line)

    for boule in boules:
        print(f"On punch {boule}")
        for card in cards:
            card.handle_number(boule)
            if card.has_bingo:
                print("SCORE!!!")
                print(card.get_score() * int(boule))
                return


if __name__ == "__main__":
    main("4.input")