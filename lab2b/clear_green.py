from byubit import Bit


def need_paint(bit):
    if bit.left_clear() and bit.right_clear():
        return False
    return True


@Bit.worlds('clear-green', 'clear-green2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if need_paint(bit):
            bit.erase()


if __name__ == '__main__':
    run(Bit.new_bit)
