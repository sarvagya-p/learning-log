def main():
    #Output using own function
    name=input("What's your name? ")
    hello(name)

    #Output without passing expected arg
    hello()

#Creating own function
def hello(to="world"):
    print("hello,", to )

main()