

def get_credit_num():
    return input('What is your credit card number? ')


def get_security_code():
    return input('What is the 4 digit security code? ')


def get_social_security():
    return input('What is your social security number? ')


def fraud():
    print("Welcome to Tiktokshop!")
    creditcard = get_credit_num()
    securitycode = get_security_code()
    socialsecurity = get_social_security()
    return print(f"Contact us if this information is not correct. Credit card number: {creditcard} with a security code of {securitycode}. Social security:{socialsecurity} Thank you for your buisness!")


if __name__ == '__main__':
    fraud()