from byubit import Bit


def jump_in_water(bit):
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()


def swim_to_treasure(bit):
    while not bit.is_red():
        bit.move()


def collect_treasure(bit):
    bit.paint("blue")


@Bit.worlds('dive-for-treasure', 'dive-for-deep-treasure')
def dive(bit):
    jump_in_water(bit)
    swim_to_treasure(bit)
    collect_treasure(bit)



if __name__ == "__main__":
    dive(Bit.new_bit)
