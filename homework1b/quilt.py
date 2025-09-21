from byubit import Bit


def red_stripe(bit):
    bit.paint("red")
    bit.left()
    bit.move()
    bit.paint("red")
    bit.move()
    bit.paint("red")

def get_back(bit):
    #get back to bottom of new row
    bit.right()
    bit.move()
    bit.right()
    bit.move()
    bit.move()
    bit.left()

def green_stripe(bit):
    bit.paint("green")
    bit.left()
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")

def green_blue_green(bit):
    bit.paint("green")
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("green")

def make_one_pattern(bit):
    red_stripe(bit)
    get_back(bit)
    green_stripe(bit)
    get_back(bit)
    green_blue_green(bit)
    get_back(bit)
    green_stripe(bit)
    get_back(bit)

@Bit.worlds("quilt")
def make_a_quilt(bit):
   make_one_pattern(bit)
   make_one_pattern(bit)
   make_one_pattern(bit)
   red_stripe(bit)
   bit.right()
   bit.right()
   bit.move()
   bit.move()
   bit.left()


if __name__ == '__main__':
    make_a_quilt(Bit.new_bit)
