def main():
    x = get_int()
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
    
main()  