from byubit import Bit


def fill_the_field(bit):
    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    while bit.front_clear():
        paint_green_stripe(bit)
        bit.move()
    paint_green_stripe(bit)


def paint_green_stripe(bit):
    bit.left()
    while bit.front_clear():
        bit.paint('green')
        bit.move()
    bit.paint('green')
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def check_for_opening(bit):
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()


@Bit.worlds('soccer', 'soccer2')
def go(bit):
    while bit.front_clear():
        fill_the_field(bit)
        check_for_opening(bit)



if __name__ == '__main__':
    go(Bit.new_bit)

