from byubit import Bit


@Bit.worlds('all-the-colors')
def all_the_colors(bit):
    bit.left()
    bit.move()
    bit.right()
    bit.paint('green')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('green')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('red')


if __name__ == '__main__':
    all_the_colors(Bit.new_bit)
