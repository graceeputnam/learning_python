from byubit import Bit


def invert_color(bit):
    if bit.is_blue():
        bit.erase()
    elif bit.is_red():
        bit.paint("red")
    elif bit.is_green():
        bit.paint("green")
    else:
        bit.paint("blue")



@Bit.worlds('invert', 'invert2', 'invert-careful')
def go(bit):
    while bit.front_clear():
        bit.move()
        invert_color(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
