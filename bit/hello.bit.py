from byubit import Bit


@Bit.empty_world(5, 3)
def move_around(bit):
 # move a couple of squares and paint red
    bit.move()
    bit.move()
    bit.paint("red")
# turn left, move up, paint green
    bit.left()
    bit.move()
    bit.paint("green")
# turn right, move, and paint blue
    bit.right()
    bit.move()
    bit.paint("blue")

    # move backwards
    move_bit_backward(bit)


def move_bit_backward(bit):
    bit.left()
    bit.left()
    bit.move()
    bit.left()
    bit.left()

if __name__ == '__main__':
    move_around(Bit.new_bit)
