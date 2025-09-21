from byubit import Bit


def in_cave(bit):
    return not bit.left_clear() and not bit.right_clear()


def maybe_turn(bit):
    if bit.is_red():
        bit.left()
    elif bit.is_blue():
        bit.right()


def get_to_cave(bit):
    """
    Bit ends just inside the mouth of the cave,
    blocked on the left and right.
    Bit turns left on red and right on blue.
    Bit paints every square green.
    """
    while not in_cave(bit):
        bit.paint('green')
        bit.move()
        maybe_turn(bit)


def at_treasure(bit):
    return bit.is_red()


def navigate_turn(bit):
    if bit.right_clear():
        bit.right()
    elif bit.left_clear():
        bit.left()


def navigate_cave(bit):
    """
    Bit starts just inside the mouth of the cave.
    Bit ends on the red square.
    Bit paints every square green.
    """
    while not at_treasure(bit):
        bit.paint("green")
        bit.move()
        navigate_turn(bit)


@Bit.worlds('treasure')
def go(bit):
    get_to_cave(bit)
    bit.snapshot("Arrived at cave!")
    navigate_cave(bit)
    bit.paint("green")


if __name__ == '__main__':
    go(Bit.new_bit)
