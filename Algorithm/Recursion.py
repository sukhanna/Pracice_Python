__author__ = 'sukhanna'
import turtle

#myTurtle = turtle.Turtle()
#myWin = turtle.Screen()
#
#def drawSpiral(myTurtle, lineLen):
#    if lineLen > 0:
#        myTurtle.forward(lineLen)
#        myTurtle.right(90)
#        drawSpiral(myTurtle,lineLen-5)
#
#drawSpiral(myTurtle,100)
#myWin.exitonclick()
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-30,t)
        t.left(40)
        tree(branchLen-30,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

#main()

# recursive way to calculate palindrome
# i.e. radar is palindrome
def is_palindrome(s, length):
    if s[0] != s[length-1]:
        return False
    elif length == 1:
        return True
    else:
        return is_palindrome(s[1:length-1], length-2)


