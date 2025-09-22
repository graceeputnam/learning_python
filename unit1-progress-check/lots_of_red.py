from byubit import Bit

def get_back(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def draw_a_line(bit):
    while bit.front_clear():
        bit.paint('red')
        bit.move()


def new_line(bit):
    bit.paint("red")
    bit.left()
    if bit.front_clear():
        bit.move()
        bit.left()
        while bit.front_clear():
            bit.move()
        bit.right()
        bit.right()


@Bit.worlds("red_field", "big_red_field")
def run(bit):
    while bit.front_clear():
        draw_a_line(bit)
        new_line(bit)
    get_back(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
