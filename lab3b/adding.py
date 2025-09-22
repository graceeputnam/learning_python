def main():
    print("I can add numbers for you!")
    while True:
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter a number: "))
        print(f"The result is: {num_1 + num_2}")
        response = input("Would you like to do more? ")
        if response == "no" or response == "No":
            break

if __name__ == '__main__':
    main()



