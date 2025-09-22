def main():
    print("Let’s concatenate strings!")
    while True:
        string_1 = input("Enter a string: ")
        string_2 = input("Enter a string: ")
        if string_1 < string_2:
            print(f"The result is: {string_1 + string_2}")
        else:
            print(f"Sorry, {string_1} is greater than {string_2}. I’m quitting.")
            break



if __name__ == '__main__':
    main()



