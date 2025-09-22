from byubit import Bit


def get_to_pool(bit):
    while not bit.right_clear() and bit.front_clear():
        bit.move()



def fill_pool(bit):
    while bit.right_clear():
        bit.right()
        while bit.front_clear():
            bit.move()
            bit.paint('blue')
        bit.left()
        bit.left()
        while bit.is_blue():
            bit.move()
        bit.right()
        bit.move()

def paint_a_red_piece(bit):
    bit.right()
    bit.move()
    bit.paint('red')


def create_flower(bit):
    if bit.front_clear():
        bit.paint('green')
        bit.left()
        bit.move()
        bit.paint('green')
        bit.move()
        bit.paint('red')
        bit.left()
        bit.move()
        bit.paint('red')
        bit.right()
        bit.move()
        paint_a_red_piece(bit)
        bit.move()
        paint_a_red_piece(bit)
        paint_a_red_piece(bit)
        bit.left()
        bit.move()
        bit.move()
        bit.left()


@Bit.worlds('blossoms', 'blossoms2')
def go(bit):
    while bit.front_clear():
        get_to_pool(bit)
        fill_pool(bit)
        create_flower(bit)



if __name__ == '__main__':
    go(Bit.new_bit)
