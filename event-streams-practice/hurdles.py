from byubit import Bit


def go_over_hurdle(bit):
    bit.left()
    while bit.front_clear():
        bit.paint('green')
        bit.move()
        if bit.right_clear():
            bit.right()
    bit.left()



@Bit.worlds('hurdles', 'hurdles2')
def run(bit):
    while bit.left_clear():
        if not bit.front_clear():
            go_over_hurdle(bit)
        else:
            bit.paint('green')
            bit.move()
    bit.paint('green')


if __name__ == '__main__':
    run(Bit.new_bit)
    
