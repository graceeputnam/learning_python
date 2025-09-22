from byubit import Bit

def movingbit(bit):
    bit.move()
    bit.move()
@Bit.empty_world(5, 8)
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

if __name__ == '__main__':
    one_firework(Bit.new_bit)

