from byubit import Bit


def climb_down(bit):
    while not bit.is_blue():
        if bit.right_clear():
            bit.right()
            bit.paint('green')
            bit.move()
            bit.left()
        else:
            bit.paint('green')
            bit.move()


def swim(bit):
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()
    bit.right()
    bit.move()


def run_to_end(bit):
    while bit.front_clear():
        bit.paint('red')
        bit.move()


@Bit.worlds('bitathon', 'bitathon2')
def run(bit):
    climb_down(bit)
    swim(bit)
    run_to_end(bit)
    bit.paint('red')


if __name__ == '__main__':
    run(Bit.new_bit)
