
def get_ratings():
    print("Enter ratings for this class.")
    print("Each rating includes a score and a comment.")
    print("Use a blank score to end.")
    responses = []
    while True:
        response = input("Score: ")
        if response == "":
            break
        comment = input("Comment: ")
        rating = (response, comment)
        responses.append(rating)
    return responses


def get_avg(ratings):
    avg = 0
    for item in ratings:
        response, comment = item
        avg = avg + float(response)
    return print(f"Average rating: {round((avg/len(ratings)), 1)}")


def share_comments(ratings):
    print("Comments:")
    for i in ratings:
        response, comment = i
        print(f"- {comment}")


def main():
    ratings = get_ratings()
    get_avg(ratings)
    share_comments(ratings)


if __name__ == '__main__':
    main()

