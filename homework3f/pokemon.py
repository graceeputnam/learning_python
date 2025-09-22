def get_pokemon():
    # return list of tuple (str,str,int)
    responses = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        type = input("Type: ")
        hp = int(input("HP: "))
        pokemon = (name, type, hp)
        responses.append(pokemon)
    return responses


def find_max(pokemon, max):
    max_pokemon = None
    max_hp = 0
    for name, type, hp in pokemon:
        if type == max:
            if hp > max_hp:
                max_hp = hp
                max_pokemon = name, type, hp
    name, type, hp = max_pokemon
    return print(f"{name} has the highest HP ({hp}) for type {type}.")


def main():
    pokemon = get_pokemon()
    max_type = input("Get max HP for type: ")
    find_max(pokemon, max_type)


if __name__ == '__main__':
    main()
#  :)
