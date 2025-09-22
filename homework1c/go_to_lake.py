from byubit import Bit


def get_to_sign(bit):
    while not bit.is_red():
        bit.paint("green")
        bit.move()
    bit.left()


def get_to_lake(bit):
    while bit.right_clear():
        bit.move()
        bit.paint("green")
    bit.move()

@Bit.worlds('go-to-lake', 'go-to-another-lake')
def go(bit):
    get_to_sign(bit)
    get_to_lake(bit)



if __name__ == "__main__":
    go(Bit.new_bit)
