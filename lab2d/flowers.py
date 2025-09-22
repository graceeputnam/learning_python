from byubit import Bit



def stem(bit, color):
    while not bit.is_green():
        bit.move()
    bit.left()
    while bit.is_green():
        bit.move()
    bit.paint(color)



def get_to_bottom(bit):
    bit.right()
    bit.right()
    bit.move()
    bit.move()
    bit.left()


def plant_flower(color, bit):
    color = bit.get_color()
    bit.erase()
    stem(bit, color)
    get_to_bottom(bit)


@Bit.worlds('flowers1', 'flowers2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if not bit.is_clear():
            plant_flower(color, bit)


if __name__ == '__main__':
    run(Bit.new_bit)
