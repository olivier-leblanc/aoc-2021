class Sub(object):

    def __init__(self):
        self.depth = 0
        self.h_pos = 0

    def handle_instruction(self, instruction):
        way = instruction[0]
        amount = int(instruction[1])

        if way == "forward":
            self.h_pos += amount
        
        elif way == "down":
            self.depth += amount

        elif way == "up":
            self.depth -= amount



def main(input_file):
    s = Sub()
    with open(input_file, "r") as f:
        
        for l in f:
            s.handle_instruction(l.replace("\n", "").split(" "))
    
    print("Réponse")
    print(s.h_pos * s.depth)

if __name__ == "__main__":
    main("2.input")