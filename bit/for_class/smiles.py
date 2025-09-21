from byubit import Bit


def draw_a_smile(bit):
    # step 1
    bit.move()
    bit.paint('blue')
    # step 2
    bit.right()
    bit.move()
    bit.move()
    bit.paint("blue")
    bit.move()
    # step 3
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.move()
    # step 4
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.move()
    bit.paint("blue")
    bit.right()

@Bit.worlds('smiles')
def run(bit):
    draw_a_smile(bit)
    bit.move()
    draw_a_smile(bit)
    bit.move()
    draw_a_smile(bit)
    bit.move()
    draw_a_smile(bit)



if __name__ == '__main__':
    run(Bit.new_bit)
