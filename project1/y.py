from byubit import Bit

def move_twice(bit):
    bit.move()
    bit.move()


def draw_top_of_y(bit):
    bit.paint('blue')
    bit.move()
    bit.right()
    bit.move()
    bit.paint('blue')
    bit.left()
    move_twice(bit)
    bit.paint('blue')
    bit.left()
    bit.move()
    bit.right()
    bit.move()
    bit.paint('blue')


def get_to_base(bit):
    bit.right()
    move_twice(bit)
    bit.right()
    move_twice(bit)
    bit.left()


def draw_base(bit):
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('blue')


def new_y_start(bit):
    bit.left()
    move_twice(bit)
    move_twice(bit)
    bit.left()
    move_twice(bit)
    move_twice(bit)
    bit.right()


def draw_full_y(bit):
    draw_top_of_y(bit)
    get_to_base(bit)
    draw_base(bit)


@Bit.worlds('y')
def paint_the_ys(bit):
    draw_full_y(bit)
    new_y_start(bit)
    bit.move()
    draw_full_y(bit)
    new_y_start(bit)
    

if __name__ == '__main__':
    paint_the_ys(Bit.new_bit)
