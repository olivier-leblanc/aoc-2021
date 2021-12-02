class Sub(object):

    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.h_pos = 0

    def handle_instruction(self, instruction):
        way = instruction[0]
        amount = int(instruction[1])

        if way == "forward":
            self.h_pos += amount
            self.depth += self.aim * amount
        
        elif way == "down":
            self.aim += amount

        elif way == "up":
            self.aim -= amount


def main(input_file):
    s = Sub()
    with open(input_file, "r") as f:
        
        for l in f:
            s.handle_instruction(l.replace("\n", "").split(" "))
    
    print("Réponse")
    print(s.h_pos * s.depth)

if __name__ == "__main__":
    main("2.input")