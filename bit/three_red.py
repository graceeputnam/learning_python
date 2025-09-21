from byubit import Bit



def three_red(bit):
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.move()
    bit.snapshot('End of three reds')


@Bit.empty_world(20, 4)
def run(bit):
    three_red(bit)
    three_red(bit)
    three_red(bit)

if __name__ == '__main__':
    run(Bit.new_bit)