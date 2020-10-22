#!/usr/bin/python3
# student: Richard J.F.P. Scholtens
# studentnr.: s2956586
# datum: 17/11/2017
# A program that designs six dice forming a straight from
# left to right in order. If someone clicks on a die it
# will show the given number of that die.

from graphics import *


def rect_maker(left_upper, right_lower, win):
    """A function that makes a white rectangle with outlining."""
    rect = Rectangle(left_upper, right_lower)
    rect.setFill('white')
    rect.draw(win)
    return rect


def dot_maker(radius):
    """A function that makes a black dot in a given radius size."""
    center = Point(0, 0)
    circle = Circle(center, radius)
    circle.setFill('black')
    return circle


def clone_mover(clone_object, x_position, y_position, win):
    """A function that clones an object and moves it to a specific position."""
    clone = clone_object.clone()
    clone.move(x_position, y_position)
    clone.draw(win)


def which_die(point, shape_lst):
    """Checks if there is a a shape found and if so it returns that shape."""
    for shape in shape_lst:
        if within_shape(point, shape):
            return shape
    return False


def within_shape(p, s):
    """Determinse whether or not the mouse click is within the shape."""
    return ((s.getP1().getX() < p.getX() < s.getP2().getX()) and
            (s.getP1().getY() < p.getY() < s.getP2().getY()))


def main():
    win = GraphWin("Straight", 500, 100)
    x1_rect = y1_rect = 20
    x2_rect = y2_rect = 80
    dice_lst = []

    for placement in range(6):
        left_up = Point(x1_rect, y1_rect)
        right_down = Point(x2_rect, y2_rect)
        dice_lst.append(rect_maker(left_up, right_down, win))
        x1_rect = x1_rect + 80
        x2_rect = x2_rect + 80

    dotsize = 5
    dot = dot_maker(dotsize)
    y_section = [30, 50, 70, 90]
    x_on30 = [110, 190, 270, 310, 350, 390, 430, 470]
    x_on50 = [50, 210, 370, 430, 470]
    x_on70 = [150, 230, 270, 310, 350, 390, 430, 470]

    for y in y_section:
        if y == 30:
            for x in x_on30:
                dotclone = clone_mover(dot, x, y, win)
        if y == 50:
            for x in x_on50:
                dotclone = clone_mover(dot, x, y, win)
        if y == 70:
            for x in x_on70:
                dotclone = clone_mover(dot, x, y, win)

    statement = True
    while statement:
        click = win.getMouse()
        counter = 0
        shape = which_die(click, dice_lst)
        if not shape:
            statement = False
        else:
            for dice in dice_lst:
                counter += 1
                if shape == dice:
                    print("You have clicked on the die: \t", counter)
    win.close()

if (__name__ == '__main__'):
    main()
