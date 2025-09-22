def get_expenses():
    response = []
    while True:
        category = input("Expense category: ")
        if category == "":
            break
        description = input("Describe the expense: ")
        amount = input("Amount: ")
        expense = category, description, amount
        response.append(expense)
    return response


def get_summary(expenses, report):
    print(f"Summary of expenses for {report}")
    total = 0
    for category, description, amount in expenses:
        if category == report:
            print(f" ${round(float(amount), 2)} - {description}")
            total = total + float(amount)
    print(f"Total: ${total}")


def main():
    expenses = get_expenses()
    report = input("What category do you want to report on? ")
    get_summary(expenses, report)


if __name__ == '__main__':
    main()
