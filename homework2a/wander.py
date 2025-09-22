from byubit import Bit


def turning_statement(bit):
    if bit.is_green():
        bit.left()
    elif bit.is_blue():
        bit.right()
    else:
        bit.paint("red")


@Bit.worlds('wander', 'wander2')
def go(bit):
    bit.paint("red")
    while bit.front_clear():
        bit.move()
        turning_statement(bit)



if __name__ == '__main__':
    go(Bit.new_bit)
