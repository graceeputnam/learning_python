from byubit import Bit

def movingbit(bit):
    bit.move()
    bit.move()

def one_firework(bit):
    bit.left()
    movingbit(bit)
    movingbit(bit)
    bit.move()
    bit.right()
    bit.move()
    bit.paint('green')
    movingbit(bit)
    bit.paint('green')
    bit.right()
    bit.move()
    bit.right()
    bit.move()
    bit.paint('red')
    bit.left()
    bit.move()
    bit.paint('green')
    movingbit(bit)
    bit.move()
    bit.left()
    movingbit(bit)


@Bit.empty_world(17, 8)
def fireworks(bit):
    one_firework(bit)
    movingbit(bit)
    one_firework(bit)
    movingbit(bit)
    one_firework(bit)


if __name__ == '__main__':
    fireworks(Bit.new_bit)