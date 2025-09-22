from byubit import Bit


def paint_flower(bit):
    if bit.is_green():
        bit.left()
        bit.move()
        bit.paint("red")
        bit.right()
        bit.right()
        bit.move()
        bit.left()


@Bit.worlds('flowers')
def go(bit):
    while bit.front_clear():
        bit.move()
        paint_flower(bit)

if __name__ == '__main__':
    go(Bit.new_bit)
