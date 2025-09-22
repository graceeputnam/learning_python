from byubit import Bit


def keep_going_guy(bit):
    if not bit.front_clear() and not bit.left_clear() and not bit.right_clear():
        return False
    return True


def need_to_turn(bit):
    if bit.front_clear():
        return True
    elif not bit.right_clear():
        bit.left()
    elif not bit.left_clear():
        bit.right()



@Bit.worlds('scurry', 'scurry2')
def go(bit):
    bit.paint("green")
    while keep_going_guy(bit):
        need_to_turn(bit)
        bit.paint('green')
        bit.move()
        if bit.is_green():
            bit.paint("blue")
            bit.move()
    bit.paint("green")


if __name__ == '__main__':
    go(Bit.new_bit)
