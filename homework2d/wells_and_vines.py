from byubit import Bit


def well(bit):
    well_color = bit.get_color()
    bit.right()
    bit.move()
    while bit.front_clear():
        bit.paint(well_color)
        bit.move()
    bit.paint(well_color)
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()


def vine(bit):
    vine_color = bit.get_color()
    bit.left()
    while bit.front_clear():
        bit.paint(vine_color)
        bit.move()
    bit.paint(vine_color)
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()


def well_or_vine(bit):
    if bit.right_clear():
        well(bit)
    elif not bit.is_on_white():
        vine(bit)


@Bit.worlds('wells-and-vines', 'wells-and-vines2')
def run(bit):
    while bit.front_clear():
        bit.move()
        well_or_vine(bit)



if __name__ == '__main__':
    run(Bit.new_bit)
