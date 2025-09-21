from byubit import Bit


def jump_up(bit):
    """ Jump up the ledge.
    Start facing the wall at the bottom of the ledge.
    End at the top, facing right, with an empty square underneath
    (Bit is not "on the ledge yet)
    """
    bit.left()
    while not bit.right_clear():
        bit.move()

    bit.right()


def go_up(bit):
    """ Get Bit to the top of the mountain.
    Bit ends at the top of the mountain facing right,
    with an empty square to his right.
    Bit paints green all squares immediately above a black square
    """
    while not bit.right_clear():
        plant_a_tree(bit)
        if not bit.front_clear():
            jump_up(bit)
        bit.move()


def jump_down(bit):
    """ Bit starts facing right with empty beneath,
    and ends facing right with black beneath.
    """
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def go_down(bit):
    """ Bit starts at the top of the mountain (facint right,
    empty space beneath) and descends to the right,
    ending in the corner.
    """
    while bit.front_clear():
        if bit.right_clear():
            jump_down(bit)

        plant_a_tree(bit)
        bit.move()


def plant_a_tree(bit):
    """ If the square below is black, plant a tree.
    """
    if not bit.right_clear():
        bit.paint("green")


@Bit.worlds('y-mountain', 'mountain')
def run(bit):
    go_up(bit)
    go_down(bit)
    bit.paint("green")


if __name__ == '__main__':
    run(Bit.new_bit)
