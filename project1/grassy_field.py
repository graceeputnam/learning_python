from byubit import Bit


def green_stripe_grass(bit):
    """
    Bit starts at bottom of empty column facing right
    Bit colors in new column
    """
    bit.paint("green")
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint("green")


def new_stripe_grass(bit):
    bit.right()
    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def get_to_the_end(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds("grassy_field", "big_grassy_field")
def run(bit):
    while bit.front_clear():
        green_stripe_grass(bit)
        new_stripe_grass(bit)
    green_stripe_grass(bit)
    get_to_the_end(bit)



if __name__ == '__main__':
    run(Bit.new_bit)
