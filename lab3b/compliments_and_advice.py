def main():
    while True:
        print("What would you like to do?")
        print(" 1) Receive compliment")
        print(" 2) Receive advice")
        print(" 3) Quit")
        response = input("Option: ")
        if response == "1":
            print("You write the best code.")
        elif response == "2":
            print("Get 8 hours of sleep every night.")
        elif response == "3":
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
