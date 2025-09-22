def get_players():
    # return list of tuple (name, age, team)
    responses = []
    while True:
        name = input("Enter player name: ")
        if name == "":
            break
        age = int(input("Enter player age: "))
        team = None
        if age > 10:
            team = "Bigs"
        elif age <= 10:
            team = "Littles"
        player = name, age, team
        responses.append(player)
    return responses


def print_team_total(players, team_name):
    print(f"Team {team_name}")
    # prints the total players
    total = 0
    for name, age, team in players:
        if team == team_name:
            total = total + 1
    print(f"Total members: {total}")


def print_team_avg(players, team_name):
    # prints the average
    total = 0
    total_age = 0
    for name, age, team in players:
        if team == team_name:
            total = total + 1
            total_age = total_age + age
    print(f"Average age: {round(total_age/total)}")


def youngest_n_oldest(players, team_name):
    # prints the youngest
    youngest = None
    for name, age, team in players:
        if team == team_name:
            if youngest is None:
                youngest = age
            elif age < youngest:
                youngest = age
    print(f"Youngest age: {youngest}")
    # prints the oldest
    oldest = None
    for name, age, team in players:
        if team == team_name:
            if oldest is None:
                oldest = age
            elif age > oldest:
                oldest = age
    print(f"Oldest age: {oldest}")


def print_members(players, team_name):
    print("Members")
    for name, age, team in players:
        if team == team_name:
            print(f" - {name} {age}")


def main():
    players = get_players()
    print_team_total(players, "Bigs")
    print_team_avg(players, "Bigs")
    youngest_n_oldest(players, "Bigs")
    print_members(players, "Bigs")
    print_team_total(players, "Littles")
    print_team_avg(players, "Littles")
    youngest_n_oldest(players, "Littles")
    print_members(players, "Littles")


if __name__ == '__main__':
    main()
# :)
