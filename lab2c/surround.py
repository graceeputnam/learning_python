from byubit import Bit


def get_to_block(bit):
    while bit.right_clear():
        bit.move()


def make_a_line(bit):
    while not bit.right_clear():
        bit.paint("green")
        bit.move()


def surround_in_green(bit):
    while not bit.is_green():
        make_a_line(bit)
        bit.right()
        bit.move()

def get_back_to_clear(bit):
    while bit.is_green():
        bit.move()


@Bit.worlds('surround', 'surround2')
def run(bit):
   while bit.front_clear():
        get_to_block(bit)
        surround_in_green(bit)
        get_back_to_clear(bit)



if __name__ == '__main__':
    run(Bit.new_bit)

