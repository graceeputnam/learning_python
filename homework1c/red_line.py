from byubit import Bit


def get_to_red(bit):
    while not bit.is_red():
        bit.move()
    bit.right()


def make_line(bit):
    bit.move()
    while not bit.is_red():
        bit.paint("red")
        bit.move()



def get_back_to_door(bit):
    bit.right()
    while bit.right_clear():
        bit.move()


@Bit.worlds('red-line')
def draw_line(bit):
    get_to_red(bit)
    make_line(bit)
    get_back_to_door(bit)


if __name__ == "__main__":
    draw_line(Bit.new_bit)

