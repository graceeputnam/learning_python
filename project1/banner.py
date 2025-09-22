from byubit import Bit


def paint_to_green(bit):
    bit.left()
    while not bit.is_green():
        bit.paint("red")
        bit.move()
    bit.paint("red")


def new_column(bit):
    bit.right()
    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()



@Bit.worlds("banner", "another_banner")
def banner(bit):
    while bit.front_clear():
        paint_to_green(bit)
        new_column(bit)

    paint_to_green(bit)
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


if __name__ == '__main__':
    banner(Bit.new_bit)
