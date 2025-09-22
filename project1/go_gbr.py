from byubit import Bit


def paint_green_until_green(bit):
    """
    Bit starts facing right on blank square
    Go until green square
    paint green until green square
    """
    while not bit.is_green():
        bit.paint("green")
        bit.move()


def paint_blue_until_blue(bit):
    """
    Bit starts on green square facing down
    Go until square is blue
    Paint blue as you go
    """
    bit.move()
    while not bit.is_blue():
        bit.paint("blue")
        bit.move()


def paint_red_until_red(bit):
    """
    Bit starts on blue square facing right
    Move bit until red square
    Paint red along the way
    """
    bit.move()
    while not bit.is_red():
        bit.paint("red")
        bit.move()


@Bit.worlds("go-go-go", "og-og-og")
def go_gbr(bit):
    paint_green_until_green(bit)
    bit.right()

    paint_blue_until_blue(bit)
    bit.left()

    paint_red_until_red(bit)



if __name__ == '__main__':
    go_gbr(Bit.new_bit)
