from byubit import Bit


def paint_the_room(bit):
    while not bit.is_blue():
        if bit.front_clear():
            bit.paint("blue")
            bit.move()
        else:
            bit.paint("blue")
            bit.left()
            bit.move()


def exit_to_car(bit):
    bit.right()
    while not bit.is_green():
        if bit.front_clear():
            bit.move()
        else:
            bit.right()


@Bit.worlds('paint-and-exit', '')
def run(bit):
    paint_the_room(bit)
    exit_to_car(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
