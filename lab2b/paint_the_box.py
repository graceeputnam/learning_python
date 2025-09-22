from byubit import Bit


def keep_going(bit):
    if  bit.is_green():
        return False
    return True


@Bit.worlds('paint-the-box', 'paint-another-box')
def run(bit):
    while keep_going(bit):
        bit.paint("green")
        bit.move()
        if not bit.front_clear():
            bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)
