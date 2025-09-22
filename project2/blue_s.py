from byubit import Bit


def draw_blue_line(bit):
    while bit.can_move_front():
        bit.paint('blue')
        bit.move()
    bit.paint('blue')


def move_a_line(bit):
    while bit.can_move_front():
        bit.move()


def draw_top_s(bit):
    bit.left()
    draw_blue_line(bit)
    bit.right()
    draw_blue_line(bit)
    bit.right()
    bit.right()
    move_a_line(bit)
    bit.left()
    move_a_line(bit)
    bit.left()


def draw_bottom_s(bit):
    bit.move()
    bit.paint('blue')
    bit.right()
    draw_blue_line(bit)
    bit.right()
    draw_blue_line(bit)
    bit.right()
    bit.right()
    move_a_line(bit)
    bit.left()
    move_a_line(bit)
    bit.right()


def draw_s(bit):
    draw_top_s(bit)
    draw_bottom_s(bit)


def check_for_s(bit):
    if bit.is_green():
        draw_s(bit)


@Bit.worlds('blue-s', 'big-blue-s')
def run(bit):
    while bit.can_move_front():
        bit.move()
        check_for_s(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
