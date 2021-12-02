

def main(file_name):
    
    with open(file_name, "r") as f:
        lines = f.readlines()

    current_mesurement = None
    increases = 1
    for l in lines:
        l = l.replace("\n", "")
        if current_mesurement is None:
            current_mesurement = l
            continue

        if l > current_mesurement:
            print(f"{l} is bigger than {current_mesurement}")
            increases += 1
        
        current_mesurement = l
    
    print(f"Number of increses {increases}")

if __name__ == "__main__":
    main("1.input")