
def get_ideas():
    responses = []
    while True:
        idea = input("Date idea: ")
        if idea == "":
            break
        cost = input("Date cost: ")
        date = (idea, cost)
        responses.append(date)
    return responses


def check_price(date, max):
    print(f"Here are all the dates below ${max}:")
    cheap_dates = []
    for idea, cost in date:
        if int(cost) <= int(max):
            cheap_dates.append((idea, cost))
    return cheap_dates


def show_dates(dates):
    for idea, cost in dates:
        print(f"- {idea} costs ${cost}.")


def main():
    date_ideas = get_ideas()
    max = input("Get max cost for date: ")
    cheap_dates = check_price(date_ideas, max)
    show_dates(cheap_dates)


if __name__ == '__main__':
    main()
