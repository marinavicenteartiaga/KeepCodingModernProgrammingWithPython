from turtle import *

miT = Turtle()


def square(side):
    miT.forward(side)
    miT.left(90)
    miT.forward(side)
    miT.left(90)
    miT.forward(side)
    miT.left(90)
    miT.forward(side)

    return side * side


area01 = square(20)
miT.down()
area02 = square(40)
miT.right(0)
area03 = square(60)
miT.left(0)
area04 = square(80)

done()
