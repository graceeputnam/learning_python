from byubit import Bit


def navigate_cave(bit):
    if bit.can_move_front():
        return
    elif bit.can_move_left():
        bit.left()
    elif bit.can_move_right():
        bit.right()


def get_through_cave(bit):
    while bit.is_empty() and bit.can_move_front():
        bit.paint('blue')
        bit.move()
        navigate_cave(bit)


def climb_moss(bit):
    bit.move()
    while bit.is_green():
        bit.move()
    bit.right()
    bit.move()


def paint_gem(bit, color):
    bit.paint(color)
    bit.move()


@Bit.worlds('escape', 'escape2')
def run(bit):
    color = bit.get_color()
    bit.paint('blue')
    bit.move()
    get_through_cave(bit)
    climb_moss(bit)
    paint_gem(bit, color)



if __name__ == '__main__':
    run(Bit.new_bit)
