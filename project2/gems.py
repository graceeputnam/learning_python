from byubit import Bit


def get_back(bit):
    bit.left()
    bit.left()
    moving_bit(bit)
    bit.right()
    bit.move()


def paint_a_line(bit, pool_color):
    while bit.can_move_front():
        bit.move()
        bit.paint(pool_color)
    bit.paint(pool_color)


def fill_the_pool(bit, pool_color):
    while bit.right_clear():
        bit.right()
        paint_a_line(bit, pool_color)
        get_back(bit)


def moving_bit(bit):
    while not bit.is_empty():
        bit.move()


@Bit.worlds('gems', 'gems2')
def run(bit):
    while bit.can_move_front():
        if not bit.is_empty():
            pool_color = bit.get_color()
            bit.erase()
        if bit.right_clear():
            fill_the_pool(bit, pool_color)
        if bit.can_move_front():
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
