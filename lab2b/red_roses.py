from byubit import Bit


def square_is_green(bit):
    if bit.is_green():
        return True
    return False


@Bit.worlds('red-roses', 'red-roses2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if square_is_green(bit):
            bit.paint('red')
        elif bit.is_blue():
            bit.paint('red')


if __name__ == '__main__':
    run(Bit.new_bit)
