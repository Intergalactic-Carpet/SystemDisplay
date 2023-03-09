import os
import time
import turtle
import psutil
import keyboard
import threading
import pyautogui
import subprocess
import configparser
from queue import Queue
from math import atan, sqrt
from time import sleep, time
# from plyer import notification
from pynput.mouse import Listener
from shapely.geometry import Polygon, Point
from win32gui import FindWindow, GetWindowRect
pressed = False
press_check = False
tim = time()
ending = False
queue = Queue()
mouse = Polygon([(0, 0), (1, 1), (-1, -1)])
screen_name = 'System Data'
turtle.title(screen_name)
graph = turtle.Turtle()
graph.hideturtle()
graph.speed(0)
text = turtle.Turtle()
text.hideturtle()
text.speed(0)
debug = False
sleep(0.1)
# interactive screen
error_folder = "Errors"
screen = turtle.Screen()
screen.tracer(False)
screen.colormode(255)
main_colour = 'black'
turtle.hideturtle()
turtle.speed(0)
main_screen = turtle.Turtle()
main_screen.fillcolor('white')
main_screen.hideturtle()
main_screen.speed(0)
text = turtle.Turtle()
text.hideturtle()
text.speed(0)
mp = turtle.Turtle()
mp.hideturtle()
mp.speed(0)
box = turtle.Turtle()
box.hideturtle()
box.speed(0)
current_screen = 'main'
text_box_input = False
text_box_clear = False
text_box_output = ''
text_box_string = ''
input_list = []
alias = ''
script_dir = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(script_dir, 'settings.ini'))
screen_dim = 960, 810
screen.title(screen_name)
screen.setup(screen_dim[0], screen_dim[1])


def draw_text(s_x, s_y, input_text, size, alter=0, rotation=0, center_rot=True):
    """
    Draws Text based on inputted parameters
    :param s_x: Top left X coordinate
    :param s_y: Top left Y coordinate
    :param input_text: Text to be drawn
    :param size: Size of the text (Max recommended: 1)
    :param alter: How much to alter the x coordinate
    :param rotation: how far tilting to the left the text should be
    :param center_rot: Whether to rotate from the center
    :return: X coordinate of the bottom right corner, Y coordinate of the bottom right corner
    """
    index = 0
    msg = str.lower(input_text)
    str_length = len(msg)
    if not center_rot:
        text.setheading(rotation)
    else:
        text.setheading(0)
        text.penup()
        text.forward((str_length / 2) * 70 * size)
        text.pendown()
        text.setheading(rotation)
    text.penup()
    text.goto(s_x - alter, s_y)
    text.pendown()
    char_functions = [la, lb, lc, ld, le, lf, lg, lh, li, lj, lk, ll, lo, lm, ln, lp, lq, lr, ls, lt, lu, lv, lw, lx,
                      ly, lz, n1, n2, n3, n4, n5, n6, n7, n8, n9, n0, period, question, apostrophe, colon, comma,
                      exclamation, quote, dollar_sign, percent_sign, under_score, left_curved_bracket,
                      right_curved_bracket, addition_sign, subtract_sign, left_square_bracket, right_square_bracket,
                      rod_thing, forward_slash, space]
    char_functions_key = "abcdefghijklomnpqrstuvwxyz1234567890.?':,!" + '"$%_()+-[]|/ '
    for i in range(str_length):
        msg2 = msg[index]
        for _ in range(len(char_functions_key)):
            if msg2 in char_functions_key[_]:
                char_functions[_](size, rotation)
        index += 1
    text.penup()
    text.right(90)
    text.forward(100 * size)
    text.pendown()
    return text.xcor(), text.ycor()


def letter_reset(size, rot):
    text.setheading(0 + rot)
    text.penup()
    text.left(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(20 * size)
    text.pendown()
    if debug:
        position = text.pos()
        print(position)


def dollar_sign(size, rot):
    ls(size, rot)
    text.penup()
    text.setheading(0 + rot)
    text.backward(70 * size)
    text.left(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(25 * size)
    text.right(90)
    text.pendown()
    text.forward(120 * size)
    text.backward(10 * size)
    text.left(90)
    text.penup()
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def percent_sign(size, rot):
    bx = text.xcor()
    by = text.ycor()
    for _ in range(10):
        text.forward(10 * size)
        text.right(90)
    text.penup()
    text.goto(bx + 50 * size, by - 100 * size)
    text.pendown()
    for _ in range(10):
        text.forward(10 * size)
        text.right(90)
    text.penup()
    text.goto(bx, by)
    text.pendown()
    forward_slash(size, rot)


def under_score(size, rot):
    text.penup()
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.pendown()
    text.forward(50 * size)
    letter_reset(size, rot)


def left_curved_bracket(size, rot):
    text.penup()
    text.right(90)
    text.forward(25 * size)
    text.left(90)
    text.pendown()
    tangent(25 * size, 25 * size, True, rot)
    text.setheading(0 + rot)
    text.forward(25 * size)
    text.penup()
    text.backward(50 * size)
    text.right(90)
    text.forward(25 * size)
    text.pendown()
    text.forward(50 * size)
    tangent(25 * size, 25 * size, False, rot)
    text.forward(25 * size)
    letter_reset(size, rot)


def right_curved_bracket(size, rot):
    text.forward(25 * size)
    tangent(25 * size, 25 * size, False, rot)
    text.right(90)
    text.forward(50 * size)
    tangent(25 * size, -25 * size, False, rot)
    text.right(180)
    text.forward(25 * size)
    text.penup()
    text.right(180)
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def addition_sign(size, rot):
    text.penup()
    text.forward(25 * size)
    text.right(90)
    text.forward(25 * size)
    text.pendown()
    text.forward(50 * size)
    text.backward(25 * size)
    text.left(90)
    text.forward(25 * size)
    text.backward(50 * size)
    text.right(90)
    text.penup()
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def left_square_bracket(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def right_square_bracket(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(50 * size)
    text.backward(50 * size)
    letter_reset(size, rot)


def back_slash(size, rot):
    tangent(100 * size, 50 * size, False, rot)
    letter_reset(size, rot)


def forward_slash(size, rot):
    text.penup()
    text.forward(50 * size)
    text.pendown()
    tangent(100 * size, -50 * size, False, rot)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def subtract_sign(size, rot):
    text.penup()
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.pendown()
    text.forward(50 * size)
    text.right(90)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def rod_thing(size, rot):
    text.penup()
    text.forward(25 * size)
    text.pendown()
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.penup()
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def la(size, rot):
    text.penup()
    text.forward(25 * size)
    text.pendown()
    tangent(100 * size, 25 * size, False, rot)
    text.penup()
    text.backward(50 * size)
    text.left(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(25 * size)
    text.pendown()
    tangent(100 * size, -25 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(12 * size)
    text.pendown()
    text.forward(25 * size)
    text.penup()
    text.forward(13 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    letter_reset(size, rot)


def lb(size, rot):
    text.forward(40 * size)
    tangent(10 * size, 10 * size, False, rot)
    text.right(90)
    text.forward(40 * size)
    text.right(90)
    text.forward(50 * size)
    text.backward(50 * size)
    text.left(90)
    text.forward(40 * size)
    text.right(90)
    tangent(10 * size, 10 * size, True, rot)
    text.right(180)
    text.forward(40 * size)
    text.right(90)
    text.forward(100 * size)
    text.backward(100 * size)
    text.right(90)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def lc(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def ld(size, rot):
    text.forward(40 * size)
    tangent(10 * size, 10 * size, False, rot)
    text.right(90)
    text.forward(80 * size)
    tangent(-10 * size, 10 * size, False, rot)
    text.backward(40 * size)
    text.left(90)
    text.forward(100 * size)
    text.backward(100 * size)
    text.right(90)
    text.forward(40 * size)
    text.penup()
    text.forward(10 * size)
    text.pendown()
    letter_reset(size, rot)


def le(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def lf(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def lg(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(25 * size)
    text.left(90)
    text.penup()
    text.forward(50 * size)
    text.left(90)
    text.pendown()
    text.forward(25 * size)
    letter_reset(size, rot)


def lh(size, rot):
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.backward(100 * size)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def li(size, rot):
    text.forward(50 * size)
    text.backward(25 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.backward(25 * size)
    text.forward(50 * size)
    letter_reset(size, rot)


def lj(size, rot):
    text.forward(50 * size)
    text.backward(25 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.backward(25 * size)
    text.right(90)
    text.backward(25 * size)
    text.forward(25 * size)
    text.left(90)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def lk(size, rot):
    text.right(90)
    text.forward(100 * size)
    text.backward(50 * size)
    text.left(90)
    text.forward(10 * size)
    tangent(50 * size, 40 * size, False, rot)
    text.left(90)
    text.penup()
    text.forward(100 * size)
    text.pendown()
    tangent(50 * size, -40 * size, False, rot)
    text.penup()
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(40 * size)
    text.pendown()
    letter_reset(size, rot)


def ll(size, rot):
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def lo(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.backward(50 * size)
    text.right(90)
    text.backward(100 * size)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def lm(size, rot):
    text.right(90)
    text.forward(100 * size)
    text.backward(100 * size)
    tangent(50 * size, 25 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(25 * size)
    text.pendown()
    text.right(90)
    text.forward(100 * size)
    text.backward(100 * size)
    tangent(50 * size, -25 * size, False, rot)
    text.penup()
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def ln(size, rot):
    text.right(90)
    text.forward(100 * size)
    text.backward(100 * size)
    tangent(100 * size, 50 * size, False, rot)
    text.left(90)
    text.forward(100 * size)
    text.backward(100 * size)
    text.right(90)
    letter_reset(size, rot)


def lp(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.backward(50 * size)
    text.forward(100 * size)
    text.left(90)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def lq(size, rot):
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.backward(50 * size)
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    letter_reset(size, rot)


def lr(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.backward(50 * size)
    text.forward(100 * size)
    text.backward(50 * size)
    tangent(50 * size, 50 * size, False, rot)
    letter_reset(size, rot)


def ls(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.backward(50 * size)
    text.forward(50 * size)
    letter_reset(size, rot)


def lt(size, rot):
    text.forward(50 * size)
    text.backward(25 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.penup()
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def lu(size, rot):
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(100 * size)
    text.backward(100 * size)
    text.right(90)
    letter_reset(size, rot)


def lv(size, rot):
    tangent(100 * size, 25 * size, False, rot)
    text.left(90)
    text.penup()
    text.forward(100 * size)
    text.right(90)
    text.forward(25 * size)
    text.pendown()
    tangent(100 * size, -25 * size, False, rot)
    text.penup()
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def lw(size, rot):
    tangent(100 * size, 12.5 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(12.5 * size)
    text.pendown()
    tangent(100 * size, -12.5 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(12.5 * size)
    text.pendown()
    tangent(100 * size, 12.5 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(12.5 * size)
    text.pendown()
    tangent(100 * size, -12.5 * size, False, rot)
    text.penup()
    text.forward(12.5 * size)
    text.pendown()
    letter_reset(size, rot)


def lx(size, rot):
    tangent(100 * size, 50 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(100 * size)
    text.pendown()
    tangent(100 * size, -50 * size, False, rot)
    text.penup()
    text.forward(50 * size)
    text.pendown()
    letter_reset(size, rot)


def ly(size, rot):
    tangent(40 * size, 25 * size, False, rot)
    text.penup()
    text.left(90)
    text.forward(40 * size)
    text.right(90)
    text.forward(25 * size)
    text.pendown()
    tangent(40 * size, -25 * size, False, rot)
    text.right(90)
    text.forward(60 * size)
    text.left(90)
    text.penup()
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def lz(size, rot):
    text.forward(50 * size)
    tangent(100 * size, -50 * size, False, rot)
    text.forward(50 * size)
    letter_reset(size, rot)


def n1(size, rot):
    text.forward(25 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.backward(25 * size)
    text.forward(50 * size)
    letter_reset(size, rot)


def n2(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def n3(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.backward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.backward(50 * size)
    text.left(180)
    letter_reset(size, rot)


def n4(size, rot):
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.backward(50 * size)
    text.forward(100 * size)
    text.left(90)
    letter_reset(size, rot)


def n5(size, rot):
    text.forward(50 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.backward(50 * size)
    text.forward(50 * size)
    letter_reset(size, rot)


def n6(size, rot):
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    text.left(90)
    text.forward(50 * size)
    letter_reset(size, rot)


def n7(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.left(90)
    letter_reset(size, rot)


def n8(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.backward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    letter_reset(size, rot)


def n9(size, rot):
    for _ in range(5):
        text.forward(50 * size)
        text.right(90)
    text.forward(100 * size)
    text.left(90)
    letter_reset(size, rot)


def n0(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(100 * size)
    text.backward(50 * size)
    text.right(90)
    text.penup()
    text.forward(22.5 * size)
    text.pendown()
    text.begin_fill()
    for _ in range(4):
        text.forward(5 * size)
        text.right(90)
    text.end_fill()
    text.penup()
    text.forward(25 * size)
    text.right(90)
    text.forward(50 * size)
    text.left(90)
    text.pendown()
    letter_reset(size, rot)


def space(size, rot):
    text.penup()
    text.forward(70 * size)
    text.pendown()
    if debug:
        position = text.pos()
        print(position, rot)


def undo():
    text.right(90)
    text.color('white')
    text.begin_fill()
    text.forward(110)
    text.right(90)
    text.forward(70)
    text.right(90)
    text.forward(110)
    text.end_fill()
    text.color('black')
    text.setheading(0)
    text.penup()
    current_x = text.xcor()
    current_line_y = text.ycor()
    new_line_y = current_line_y + 120
    if current_x < -351:
        text.goto(350, new_line_y)
    if new_line_y > 301:
        text.sety(300)
    text.pendown()
    if debug:
        position = text.pos()
        print(position)


def tangent(tangent_height, tangent_width, custom_angle, rot):
    if not custom_angle:
        text.setheading(270 + rot)
    angle = atan(tangent_width / tangent_height)
    angle = angle * 57.295779513082321578272654463367
    text.left(angle)
    if debug:
        print(angle)
    length = tangent_height * tangent_height + tangent_width * tangent_width
    length = sqrt(length)
    text.forward(length)
    if debug:
        print(length)
    text.setheading(rot)


def period(size, rot):
    text.penup()
    text.backward(15 * size)
    text.right(90)
    text.forward(90 * size)
    text.pendown()
    text.begin_fill()
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.right(90)
    text.end_fill()
    text.penup()
    text.forward(90 * size)
    text.right(90)
    text.forward(15 * size)
    text.pendown()
    if debug:
        print(rot)


def comma(size, rot):
    text.penup()
    text.backward(15 * size)
    text.right(90)
    text.forward(95 * size)
    text.pendown()
    text.begin_fill()
    text.forward(10 * size)
    text.left(90)
    text.forward(5 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(5 * size)
    text.right(90)
    text.end_fill()
    text.penup()
    text.forward(95 * size)
    text.right(90)
    text.forward(15 * size)
    text.pendown()
    if debug:
        print(rot)


def apostrophe(size, rot):
    text.penup()
    text.backward(5 * size)
    text.pendown()
    text.begin_fill()
    text.right(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(5 * size)
    text.right(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(5 * size)
    text.end_fill()
    text.penup()
    text.forward(5 * size)
    text.pendown()
    if debug:
        print(rot)


def quote(size, rot):
    text.penup()
    text.backward(5 * size)
    text.pendown()
    text.begin_fill()
    text.right(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(5 * size)
    text.right(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(5 * size)
    text.end_fill()
    text.penup()
    text.backward(2 * size)
    text.pendown()
    text.penup()
    text.backward(5 * size)
    text.pendown()
    text.begin_fill()
    text.right(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(5 * size)
    text.right(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(5 * size)
    text.end_fill()
    text.penup()
    text.forward(12 * size)
    text.pendown()
    if debug:
        print(rot)


def question(size, rot):
    text.forward(50 * size)
    text.right(90)
    text.forward(50 * size)
    text.right(90)
    text.forward(25 * size)
    text.left(90)
    text.forward(40 * size)
    text.penup()
    text.forward(5 * size)
    text.pendown()
    text.pensize(5 * size)
    text.forward(5 * size)
    text.pensize(1)
    text.penup()
    text.left(90)
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def exclamation(size, rot):
    text.penup()
    text.forward(25 * size)
    text.pendown()
    text.right(90)
    text.forward(70 * size)
    text.penup()
    text.forward(10 * size)
    text.pendown()
    text.forward(25 * size)
    text.left(90)
    text.penup()
    text.forward(25 * size)
    text.pendown()
    letter_reset(size, rot)


def colon(size, rot):
    text.penup()
    text.backward(15 * size)
    text.right(90)
    text.forward(90 * size)
    text.pendown()
    text.begin_fill()
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.right(90)
    text.end_fill()
    text.penup()
    text.forward(80 * size)
    text.right(90)
    text.pendown()
    text.begin_fill()
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.right(90)
    text.end_fill()
    text.penup()
    text.right(180)
    text.forward(10 * size)
    text.left(90)
    text.forward(10 * size)
    text.right(90)
    text.forward(10 * size)
    text.pendown()
    if debug:
        print(rot)


class CreateGraph:
    """
    :param xcor: The bottom left x position of the graph
    :param ycor: The bottom left y position of the graph
    :param width: The width of the graph
    :param height: The height of the graph
    :param max_var_on_display: How many variables on display at a time (0 == infinity)
    :param initial_var: an initial number to start it off (not required)
    :param dot: Whether dots are displayed
    :param line: Whether graph lines are displayed
    :param side_increment: The vertical scale increment (may not work as intended)
    :param low_scale: The horizontal scale (doesn't look very good at the moment)
    :param side_scale: The vertical scale
    :param line_scale: The lines marking the left and bottom
    :param box_: Whether the graph is encased in a box
    :param max_points: How many points to be stored (erases old points if exceeded, 0 == infinity)
    :param last_point_bar: A line extending from the last point to the xcor
    :param last_point_bar_colour: Colour of the last point bar
    :param scale_colour: Colour of the scale
    :param line_colour: Colour of the line
    :param dot_colour: Colour of the dots
    :param all_point_bar: A line extending from each point to the xcor
    :param broken_graphics: A which when True, can make some interesting optical illusions
        (depending on point positions)
    :param fancy_graphics: Curvy lines (doesn't work as intended yet)
    :param max_high: The Maximum High
    """

    def __init__(self, xcor, ycor, width, height, max_var_on_display=0, initial_var=0, dot=False, line=True,
                 side_increment=10, low_scale=False, side_scale=True, line_scale=True, box_=False, max_points=200,
                 last_point_bar=False, last_point_bar_colour='midnightblue', scale_colour='black', line_colour='black',
                 dot_colour='black', all_point_bar=False, broken_graphics=False, fancy_graphics=False,
                 show_decimals_on_side=True, max_high=float('inf'), man_high=0, refuse_same=False):
        self.last_point_bar = last_point_bar
        self.show_decimal = show_decimals_on_side
        self.fancy_graphics = fancy_graphics
        self.broken = broken_graphics
        self.last_point_bar_colour = last_point_bar_colour
        self.all_point_bar = all_point_bar
        self.scale_colour = scale_colour
        self.line_colour = line_colour
        self.dot_colour = dot_colour
        self.max_high = max_high
        self.man_high = man_high
        if max_var_on_display == 0:
            max_var_on_display = float('inf')
        if height <= 15:
            height = 16
        self.line_scale = line_scale
        self.box = box_
        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.height = height
        self.var = [initial_var]
        self.increment = width / len(self.var)
        self.high = 1
        self.low = 0
        self.v_distance = height / self.high
        self.new = True
        self.max_var = max_var_on_display
        self.display_var = self.var
        self.dot = dot
        self.line = line
        self.si = side_increment
        self.side_scale = side_scale
        self.lower_scale = low_scale
        if max_points < self.max_var:
            max_points = self.max_var
        self.max_points = max_points
        self.rs = refuse_same

    def update_data(self):
        self.v_distance = self.height / self.high
        if len(self.var) > self.max_var:
            count = 0
            self.display_var = []
            for _ in range(len(self.var)):
                if count >= len(self.var) - self.max_var:
                    temp_var = str(self.var[count])
                    self.display_var = self.display_var + [temp_var]
                count += 1
        else:
            self.display_var = self.var
        if self.max_var == float('inf'):
            self.increment = self.width / len(self.display_var)
        else:
            self.increment = self.width / self.max_var

    def update_graph(self, var):
        if float(var) > self.man_high != 0:
            var = self.high
        if len(self.var) == 1 and self.new:
            self.new = False
            self.var = [var]
        elif not (self.rs and str(self.var[-1]) == str(var)):
            self.var = self.var + [str(var)]
        if self.max_points < 10:
            self.max_points = 10
        if len(self.var) > self.max_points:
            v = []
            for _ in range(len(self.var)):
                if _ >= (len(self.var) - self.max_points):
                    v = v + [self.var[_]]
            self.var = v
        self.var = all_float(self.var)
        self.high, self.low = float(max(self.var)), float(min(self.var))
        if self.man_high != 0:
            self.high = self.man_high
        elif self.high > self.max_high:
            self.high = self.max_high
        if self.high == 0:
            self.high = 1
        self.v_distance = self.height / self.high

    def reset_graph(self):
        self.high = 1
        self.low = 1
        self.var = [0]
        self.display_var = self.var

    def draw_graph(self):
        self.update_data()
        if self.high * self.v_distance > self.height:
            self.v_distance -= 1
        count = 0
        if self.line_scale or self.box:
            graph.color(self.scale_colour)
            graph.penup()
            graph.setheading(0)
            graph.setpos(self.xcor, self.ycor)
            graph.pendown()
            graph.left(90)
            graph.forward(self.height)
            graph.backward(self.height)
            graph.right(90)
            graph.forward(self.width)
        if self.box:
            graph.left(90)
            graph.forward(self.height)
            graph.left(90)
            graph.forward(self.width)
        graph.penup()
        graph.setpos(self.xcor, self.ycor)
        graph.pendown()
        if self.side_scale:
            graph.color(self.scale_colour)
            scale = self.height / 16
            si = self.height / scale
            for _ in range(remove_decimal(scale)):
                text_ = round_to((self.high / scale) * (_ + 1))
                if len(self.var) > 50:
                    text_ = round_10(float(text_))
                if len(str(text_)) > 1:
                    if str(text_)[-1] == '0' and str(text_)[-2] == '.':
                        text_ = int(remove_decimal(text_))
                    else:
                        text_ = float(text_)
                else:
                    text_ = float(text_)
                text_ = f'{text_} - '
                text.color(self.scale_colour)
                if _ == 0 and self.low >= 0:
                    draw_text(self.xcor - len('0 - ') * 7, self.ycor + 5, '0 - ', 0.1)
                draw_text(self.xcor - len(text_) * 7, (self.ycor + 20) + si * _ * 1.02, text_, 0.1)
        for _ in range(len(self.display_var)):
            if _ == 0 or not self.line:
                graph.penup()
            temp_var = float(self.display_var[count])
            graph.color(self.line_colour)
            gx = (self.increment * count) + 4 + self.xcor
            gy = (temp_var / self.high) * self.height + float(self.ycor)
            if not self.fancy_graphics:
                graph.setx(gx)
                graph.sety(gy)
            else:
                while not (close_to(graph.xcor(), gx, 1) and close_to(graph.ycor(), gy, 1)):
                    x = (gx - graph.xcor()) / 10
                    y = (gy - graph.ycor()) / 8
                    graph.setpos(graph.xcor() + x, graph.ycor() + y)
            if _ == 0 or not self.line:
                graph.pendown()
            graph.penup()
            graph.setheading(90)
            graph.backward(1)
            graph.pendown()
            if self.dot:
                graph.begin_fill()
                graph.circle(2)
                graph.end_fill()
            graph.penup()
            graph.setheading(90)
            graph.forward(1)
            graph.pendown()
            if self.last_point_bar and _ == len(self.display_var) - 1 or self.all_point_bar:
                a = graph.xcor() - self.xcor
                graph.color(self.last_point_bar_colour)
                graph.setheading(0)
                graph.backward(a)
                if not self.broken:
                    graph.forward(a)
            count += 1
        if self.lower_scale:
            graph.color(self.scale_colour)
            points = remove_decimal(self.width / 7)
            for _ in range(remove_decimal(points / 2)):
                t_ = '|'
                draw_text(self.xcor + 14 * _ + 5, self.ycor - 5, t_, 0.1, len(t_) / 2)


def all_float(in_):
    out_ = []
    for _ in range(len(in_)):
        try:
            out_ = out_ + [float(in_[_])]
        except ValueError:
            out_ = out_ + [0]
    return out_


def round_to(in_, decimal=1):
    in_ = str(in_)
    decimal_index = None
    out = ''
    for _ in range(len(in_)):
        if '.' in in_[_]:
            decimal_index = _
            out = out + in_[_]
        elif decimal_index is None:
            out = out + in_[_]
        elif _ <= decimal_index + decimal:
            out = out + in_[_]
    return out


def find_high_low(var):
    high = remove_decimal(var[0])
    low = remove_decimal(var[0])
    for _ in range(len(var)):
        z_ = remove_decimal(var[_])
        if z_ > high:
            high = z_
        elif z_ < low:
            low = z_
    return high, low


def remove_decimal(in_):
    in_ = str(in_)
    out_ = ''
    for _ in range(len(in_)):
        if '.' not in in_[_]:
            out_ = out_ + in_[_]
        else:
            break
    return int(out_)


def close_to(var, var2, thresh):
    re = False
    if thresh > (var - var2) > -thresh:
        re = True
    return re


def find_and_filter_out(in_, rejected):
    in_ = str(in_)
    out_ = ''
    for _ in range(len(in_)):
        if rejected not in in_[_]:
            out_ = out_ + in_[_]
    return out_


def round_10(round_):
    if round_ > 10 or round_ < -10:
        round_ = str(remove_decimal(round_))
        if int(round_[-1]) > 4:
            mid = str(int(round_[-2]) + 1)
        else:
            mid = str((round_[-2]))
        for _ in range(2):
            round_ = remove_text(round_, len(round_) - 1)
        round_ = float(str(round_) + mid + '0')
    elif 10 > round_ > 0:
        round_ = str(remove_decimal(round_))
        if int(round_[-1]) > 4:
            round_ = '10'
        else:
            round_ = '0'
    elif -10 < round_ < 0:
        round_ = str(remove_decimal(round_))
        if int(round_[-1]) > 4:
            round_ = '-10'
        else:
            round_ = '0'
    else:
        if round_ < 0:
            round_ = '-' + str(remove_decimal(round_))
        else:
            round_ = str(remove_decimal(round_))
    return round_


def remove_text(text_, point):
    output = ''
    for _ in range(len(text_)):
        if _ != point:
            output = output + text_[_]
    return output


def number_converter(num_input):
    """
    Removes all characters except numbers and periods
    :param num_input: String to convert
    :return: Number
    """
    num_input = str(num_input)
    num_len = len(num_input)
    allowed_chars = '1234567890.'
    chars_length = len(allowed_chars)
    index = 0
    output = ''
    for _ in range(num_len):
        indexed = num_input[index]
        index_2 = 0
        for i in range(chars_length):
            second_indexed = allowed_chars[index_2]
            if indexed in second_indexed:
                output = output + indexed
            index_2 += 1
        index += 1
    return output


def test_for(test, match):
    return str(match) in str(test)


def replace_index(string_or_list, replacement, index, is_list):
    in_ = string_or_list
    if is_list:
        out = []
        for _ in range(len(in_)):
            if _ == index:
                out = out + [replacement]
            else:
                out = out + [in_[_]]
    else:
        out = ''
        for _ in range(len(in_)):
            if _ == index:
                out = out + replacement
            else:
                out = out + in_[_]
    return out


def replace_instance(string_or_list, replacement, is_list, target):
    in_ = string_or_list
    if is_list:
        out = []
        for _ in range(len(in_)):
            out2 = ''
            for i in range(len(in_[_])):
                if target in in_[_][i]:
                    out2 = out2 + replacement
                else:
                    out2 = out2 + in_[_][i]
            out = out + [out2]
    else:
        out = ''
        for _ in range(len(in_)):
            if target in in_[_]:
                out = out + replacement
            else:
                out = out + in_[_]
    return out


def swap_chars(string_, rep_a, rep_b):
    out = ''
    for _ in range(len(string_)):
        if rep_a in string_[_]:
            out = out + rep_b
        elif rep_b in string_[_]:
            out = out + rep_a
        else:
            out = out + string_[_]
    return out


def text_filter(text_input, allowed_chars):
    """
    Removes all characters that aren't specified as allowed
    :param text_input: The text to be filtered
    :param allowed_chars: The characters allowed in the text
    :return: The filtered text
    """
    text_input = str.lower(str(text_input))
    text_length = len(text_input)
    chars_length = len(allowed_chars)
    index = 0
    output = ''
    for _ in range(text_length):
        indexed = text_input[index]
        index_2 = 0
        for i in range(chars_length):
            second_indexed = allowed_chars[index_2]
            if indexed in second_indexed:
                output = output + indexed
            index_2 += 1
        index += 1
    return output


def draw_legend(x_, y, size, list_of_values):
    vals = list_of_values
    b = 0
    for _ in range(len(vals)):
        if _ == len(vals) - 1:
            b = b + len(vals[_][0]) * (70 * size)
        else:
            b = b + len(vals[_][0]) * (70 * size) + 70 * size
    x_ = x_ - b / 2
    for _ in range(len(vals)):
        text.color(vals[_][1])
        if _ == 0:
            z = 0
        else:
            z = 70 * size
        x_, y_ = draw_text(x_ + z, y, vals[_][0], size)


def draw_label(text_to_calc, text_to_print, label_x, label_y, size, orientation, greyed_out=False, colour='null',
               bold=False, bounding=False):
    """
    Draws a label based on parameters and returns if the button is pressed
    :param text_to_calc: The text to be calculated for the bounding, collisions, and orientation
    :param text_to_print: The text that is printed
    :param label_x: Top Left corner X coordinate
    :param label_y: Top Left corner Y coordinate
    :param size: Size of the text
    :param orientation: If it's centered or not, a value of -1 keeps the top left corner of the text relative to the
     given coordinates, while a value of 0 centers the text
    :param greyed_out: Whether the text and bounding is grey or not, if True the button turns grey and the contact value
     is set to False
    :param colour: Colour of the text and bounding
    :param bold: Whether the text is bold
    :param bounding: Whether a box surrounds the text
    :return: Whether the button has been clicked (contact)
    """
    global custom_label
    custom_label = CreateButton(text_to_calc, text_to_print, label_x, label_y, size, orientation, bounding, greyed_out,
                                colour, bold)
    contact = custom_label.draw_button()
    return contact


class CreateButton:
    """
    Defines the button parameters according to the inputted information
    """

    def __init__(self, text_to_calc, text_to_print, button_x, button_y, size, orientation, bounding, greyed_out,
                 colour, bold):
        self.text_to_calc = text_to_calc
        self.text_to_print = text_to_print
        self.bx = button_x
        self.by = button_y
        self.size = size
        self.orientation = orientation
        self.bounding = bounding
        self.greyed = greyed_out
        self.bold = bold
        if 'null' in colour:
            self.colour = main_colour
        else:
            self.colour = colour
        spacing = 10
        if debug:
            print(f'Button Parameters: {self.text_to_calc}, {self.text_to_print}, {self.bx}, {self.by},'
                  f' {spacing}, {self.size}, {self.orientation}, {self.bounding}')
        main_screen.pencolor(self.colour)
        text.pencolor(self.colour)
        text_input = str.lower(str(text_to_calc))
        text_length = len(text_input)
        allowed_chars = 'abcdefghijklomnpqrstuvwxyz1234567890 ><-[]|_()!+%$'
        chars_length = len(allowed_chars)
        index = 0
        output = ''
        for _ in range(text_length):
            indexed = text_input[index]
            index_2 = 0
            for i in range(chars_length):
                second_indexed = allowed_chars[index_2]
                if indexed in second_indexed:
                    output = output + indexed
                index_2 += 1
            index += 1
        conditioned_len = len(output)
        final_x = self.bx + (conditioned_len * 70) * self.size
        final_y = self.by - (100 * self.size)
        if self.orientation == 0:
            alter = final_x / 2
        else:
            alter = 0
        if debug or debug:
            print('fx', final_x, 'fy', final_y, 'bx', button_x, 'by', button_y, 'alt', alter)
        draw_text(self.bx, self.by, self.text_to_print, self.size, alter)
        bound = Polygon([((self.bx - spacing) - alter, self.by + spacing),
                         ((final_x + spacing) - alter, self.by + spacing),
                         ((final_x + spacing) - alter, final_y - spacing),
                         ((self.bx - spacing) - alter, final_y - spacing)])
        self.final_x = final_x
        self.final_y = final_y
        self.spacing = spacing
        self.alter = alter
        self.bound = bound

    def draw_button(self):
        """
        Draws the button based on the previously inputted information
        """
        if self.bold:
            text.pensize(7)
        else:
            text.pensize(1)
        if self.greyed:
            text.color('grey')
            main_screen.pencolor('grey')
        else:
            text.color(self.colour)
            main_screen.pencolor(main_colour)
        contact = mouse.intersects(self.bound)
        if contact and not self.greyed:
            spacing = 15
        else:
            spacing = 10
        if self.bounding:
            main_screen.penup()
            main_screen.goto((self.bx - spacing) - self.alter, self.by + spacing)
            main_screen.begin_fill()
            main_screen.pendown()
            main_screen.goto((self.final_x + spacing) - self.alter, self.by + spacing)
            main_screen.goto((self.final_x + spacing) - self.alter, self.final_y - spacing)
            main_screen.goto((self.bx - spacing) - self.alter, self.final_y - spacing)
            main_screen.goto((self.bx - spacing) - self.alter, self.by + spacing)
            main_screen.end_fill()
        draw_text(self.bx, self.by, self.text_to_print, self.size, self.alter)
        text.pencolor(self.colour)
        main_screen.pencolor(main_colour)
        if self.greyed:
            contact = False
        return contact


def extract_decimal(in_):
    ints = ''
    dec_found = False
    dec_count = 2
    for _ in range(len(str(in_))):
        if str(in_)[_] == '.':
            dec_found = True
        elif not dec_found:
            ints = ints + str(in_)[_]
        else:
            dec_count += 1
    ints = int(ints)
    in_ = in_ - ints
    out_ = ''
    for _ in range(dec_count):
        out_ = out_ + str(in_)[_]
    return float(out_)


def read_file(source, index=None):
    try:
        with open(source, 'r') as file:
            if index is None:
                out = file.readlines()
            else:
                out = file.readlines()[index]
            file.close()
    except IndexError:
        out = None
    return out


def send_notification(title, message, time_out=5):
    if debug:
        print(title, message, time_out)
    # notification.notify(title= 'System Data - ' + title, message=message, app_name="System Data", timeout=time_out)


def extract_setting(content, typ):
    # For text files
    data = ''
    extract = False
    for _ in range(len(content)):
        if extract:
            data = data + content[_]
        elif content[_] == ':':
            extract = True
    if typ == 'int':
        try:
            data = float(data)
        except ValueError:
            data = None
    elif typ == 'bool':
        if 'true' in data:
            data = True
        else:
            data = False
    return data


def get_settings(settings, path='settings.ini'):
    """
    Extracts settings from settings.ini and formats them into an immediately usable format.
    :param settings: Format - [(default setting, ('setting section', 'setting name'), 'type of variable (int/bool)')]
    :param path: Path to settings (relative)
    """
    path = os.path.join(script_dir, path)
    config.read(path)
    data = []
    for _ in range(len(settings)):
        setting = settings[_][0]
        if 'int' in settings[_][2]:
            try:
                setting = config.getfloat(settings[_][1][0], settings[_][1][1])
            except configparser.NoSectionError:
                print(f'Setting Section {settings[_][1][0]} missing')
            except configparser.NoOptionError:
                print(f'Setting {settings[_][1][1]} Missing')
            except ValueError:
                print(f'Setting "{config.get(settings[_][1][0], settings[_][1][1], fallback="unknown")}" in '
                      f'{settings[_][1][0]}, {settings[_][1][1]} is invalid')
            except configparser.Error:
                print('An error reading settings has occurred')
        elif 'bool' in settings[_][2]:
            try:
                setting = config.get(settings[_][1][0], settings[_][1][1])
                if 'true' in str.lower(str(setting)):
                    setting = True
                else:
                    setting = False
            except configparser.NoSectionError:
                print(f'Setting Section {settings[_][1][0]} missing')
            except configparser.NoOptionError:
                print(f'Setting {settings[_][1][1]} Missing')
            except ValueError:
                print(f'Setting {settings[_][0]} in {settings[_][1][0]}, {settings[_][1][1]} invalid')
            except configparser.Error:
                print('An error reading settings has occurred')
        data = data + [setting]

    return data


def error_msg(code, error=None):
    if error:
        pass
    st = f'Error Code: {code}'
    if error is not None:
        st = st + f'. {error} error'
    print(st)


def set_settings(settings, path='settings.ini'):
    """
    Extracts settings from settings.ini and formats them into an immediately usable format.
    :param settings: Format - [(setting, ('setting section', 'setting name'))]
    :param path: Path to settings (relative)
    """
    path = os.path.join(script_dir, path)
    config.read(path)
    for _ in range(len(settings)):
        section = settings[_][1][0]
        name = settings[_][1][1]
        setting = settings[_][0]
        try:
            config.set(section, name, setting)
        except configparser.NoSectionError:
            error_msg(1, 'File Section')
        except configparser.NoOptionError:
            error_msg(1, 'File')
        except configparser.Error:
            error_msg(0, 'Unknown')

    with open(path, 'w') as f:
        config.write(f)


def toggle(in_):
    if in_:
        out = False
    else:
        out = True
    return out


def if_pressed():
    return pressed and not press_check


def start():
    global ending, debug, pressed, press_check
    rs = get_settings([(False, ('other', 'rs'), 'bool')])
    rec = 30
    turtle.Screen().tracer(False)
    data = get_settings([(rec, ('gl', 'gpu'), 'int'), (rec, ('gl', 'cpu'), 'int'), (rec, ('gl', 'ram'), 'int')])
    rl_gpu = data[0]
    rl_cpu = data[1]
    rl_ram = data[2]
    debug = False
    cpu_g = CreateGraph(-200, 200, 400, 100, max_points=rl_cpu, max_var_on_display=rl_cpu, man_high=100)
    ram_g = CreateGraph(-200, 50, 400, 100, max_points=rl_ram, max_var_on_display=rl_ram, man_high=100)
    gpu = CreateGraph(-200, 50, 400, 100, max_points=rl_gpu, max_var_on_display=rl_gpu, man_high=100)
    gpu_ = Throttling(get_gpu_usage, start_=0, timing=0.1)
    count = 0
    turtle.fillcolor('grey')
    batt_a = TargetController(0, transition_time=1)
    fps_g = CreateGraph(-200, -350, 400, 100, max_points=50, max_var_on_display=50)
    elapsed = 0.1
    ending = False
    stop_count = 0
    switch = False
    switch2 = False
    fps_n = NumberAverager(10)
    s1 = CreateButton(f'Switch', f'Switch', -300, 110, 0.1, -1, bold=False, colour=main_colour,
                      greyed_out=False, bounding=True)
    s2 = CreateButton(f'Switch', f'Switch', -300, 260, 0.1, -1, bold=False, colour=main_colour,
                      greyed_out=True, bounding=True)
    while True:
        start_ = time()
        if pressed:
            if not press_check:
                pressed = True
                press_check = True
            else:
                pressed = False
        else:
            pressed = False
            press_check = False
        if rs:
            data = get_settings([(rec, ('gl', 'gpu'), 'int'), (rec, ('gl', 'cpu'), 'int'), (rec, ('gl', 'ram'), 'int')])
            rl_gpu = data[0]
            rl_cpu = data[1]
            rl_ram = data[2]
            cpu_g.max_var = rl_cpu
            cpu_g.max_points = rl_cpu
            ram_g.max_points = rl_ram
            ram_g.max_var = rl_ram
            gpu.max_var = rl_gpu
            gpu.max_points = rl_gpu
        graph.clear()
        text.clear()
        turtle.clear()
        main_screen.clear()
        cpu_d = read_file(os.path.join(script_dir, 'cpu bridge.txt'), 0)
        if cpu_d is None:
            cpu_d = 0
        else:
            try:
                cpu_d = float(cpu_d)
            except ValueError:
                print(f'CPU ValueError: could not convert string to float: {cpu_d}')
        if keyboard.is_pressed('t') and keyboard.is_pressed('ctrl'):
            if not keyboard.is_pressed('shift'):
                cpu_d = 100
            else:
                cpu_d = 0
        cpu_c = cpu_d
        cpu_g.update_graph(cpu_c)
        ram = round_to(psutil.virtual_memory()[2], 0.1)
        if keyboard.is_pressed('t') and keyboard.is_pressed('ctrl'):
            if not keyboard.is_pressed('shift'):
                ram = 100
            else:
                ram = 0
        if ending:
            ram = 0
        ram_c = ram
        ram_g.update_graph(ram_c)
        gpu_.update()
        gpu_c = gpu_.store
        gpu_c = ave(gpu_c)
        gpu.update_graph(gpu_c)
        if count > 50:
            cpu_g.draw_graph()
            draw_label(f'{round_to(0, 1)}% CPU Util', f'{round_to(cpu_c, 1)}% CPU Util', 220, 270,
                       0.2, -1, False)
            if switch:
                gpu.draw_graph()
                draw_label(f'{gpu_c}% GPU Util', f'{gpu_c}% GPU Util', 220, 100, 0.2, -1, False)
            else:
                ram_g.draw_graph()
                draw_label(f'{ram_c}% RAM Util', f'{ram_c}% RAM Util', 220, 100, 0.2, -1, False)
            s1.draw_button()
            s2.draw_button()
            x, y = mp.pos()
            if if_pressed() and s1.bound.contains(Point(x, y)):
                switch = toggle(switch)

            if if_pressed() and s2.bound.contains(Point(x, y)):
                switch2 = toggle(switch2)

        else:
            draw_label('Loading', 'Loading', 0, 50, 0.3, 0)
        batt = float(psutil.sensors_battery()[0])
        # batt graph
        if keyboard.is_pressed('t') and keyboard.is_pressed('ctrl'):
            if not keyboard.is_pressed('shift'):
                batt = 100
            else:
                batt = 0
        if ending:
            batt = 0
        batt_dis = batt * 4
        batt_a.change_target(batt_dis)
        batt_a.update(elapsed)
        batt_dis = batt_a.output
        batt_b = batt_a.output / 4
        if batt_dis < 0:
            batt_dis = 0
        if batt_b > 99.9:
            turtle.fillcolor('limegreen')
        else:
            turtle.fillcolor('grey')
        if count > 50:
            add = 'remaining'
            if batt_b >= 99.9:
                add = 'charged'
                batt_b = 100
            draw_label(f'{round_to(batt_b, 1)}% {add}', f'{round_to(batt_b, 1)}% {add}', 220, -40, 0.2, -1,
                       False)
            turtle.setheading(0)
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(-200, 0)
            turtle.forward(batt_dis)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(batt_dis)
            turtle.goto(-200, -100)
            turtle.end_fill()

            turtle.fillcolor('white')
            turtle.pencolor('black')
            turtle.penup()
            turtle.goto(190, 0)
            turtle.begin_fill()
            turtle.goto(190, -25)
            turtle.goto(200, -25)
            turtle.goto(200, 0)
            turtle.end_fill()
            turtle.goto(190, -75)
            turtle.begin_fill()
            turtle.goto(190, -100)
            turtle.goto(200, -100)
            turtle.goto(200, -75)
            turtle.end_fill()

            turtle.goto(-200, 0)
            turtle.goto(190, -25)
            turtle.pendown()
            turtle.goto(200, -25)
            turtle.goto(200, -75)
            turtle.goto(190, -75)
            turtle.penup()
            turtle.goto(-200, 0)
            turtle.pendown()
            turtle.goto(190, 0)
            turtle.goto(190, -100)
            turtle.goto(-200, -100)
            turtle.goto(-200, 0)
        # charge sign
        batt2 = psutil.sensors_battery()[2]
        if batt_b > 99.9:
            text_ = 'Fully Charged'
        elif batt2:
            text_ = 'Charging'
        elif batt2 is None:
            text_ = 'AC Status Unknown'
        else:
            hr = (psutil.sensors_battery()[1] / 60) / 60
            mi = extract_decimal(hr) * 60
            if hr < 1000:
                text_ = f'{remove_decimal(hr)}hrs, {remove_decimal(mi)}mins left'
            else:
                text_ = 'Calculating time left'
        if count > 50:
            draw_label(text_, text_, 0, -115, 0.2, 0, False)
        if count <= 100:
            count += 1
        if keyboard.is_pressed('x') and count > 50:
            stop_count += (100 - stop_count) / 4
        elif stop_count > 0:
            stop_count += -stop_count / 2
        if stop_count > 99:
            ending = True
            write_file(1, 'cpu_stop.txt')
        if stop_count > 99 or ending:
            stop_count = 100
        if count > 50:
            draw_stop(stop_count, ending)
        if ending:
            break

        # mp.clear()
        mp.penup()
        mp.setpos(get_mouse())
        # mp.pendown()
        # mp.dot(10)
        draw_label('', f'{round_to(fps_n.get_average(), 1)} FPS', -400, -200, 0.2, -1)
        fps_n.add_number(1 / elapsed)
        fps_g.update_graph(fps_n.get_average())
        # fps_g.draw_graph()
        # draw_label('', f'{round_to(get_change(fps_g.var), 4)}', -400, -300, 0.2, -1)
        turtle.Screen().update()
        end = time()
        elapsed = end - start_
    end_it()


def get_change(inputs):
    return inputs[-1] - inputs[0]


def ave(items):
    try:
        if len(items) > 1:
            al = 0
            __ = 0
            for _ in range(len(items)):
                __ = _
                try:
                    al += float(items[_])
                except ValueError:
                    pass
            out = al / __
        else:
            out = items[0]
    except TypeError:
        out = items
    return out


def draw_stop(val, ending_):
    if ending_:
        val = 100
    z = remove_decimal(255 * (val / 100))
    turtle.color('grey')
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.goto(200, -200)
    turtle.goto(200, -220)
    turtle.goto(-200, -220)
    turtle.goto(-200, -200)
    if val > 1:
        turtle.color((237, 168, 168))
        turtle.begin_fill()
        turtle.goto(-200 + 4 * val, -200)
        turtle.sety(-220)
        turtle.setx(-200)
        turtle.end_fill()
        turtle.color('grey')
    draw_label('Hold X to Stop', 'Hold X to Stop', 0, -202.5, size=0.15, orientation=0, colour=(z, z, z))
    return


def get_gpu_usage():
    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv"]).decode("utf-8")
        gpu_usage = [int(x.split()[0]) for x in output.strip().split("\n")[1:]]
        return gpu_usage
    except Exception as e:
        print("Error getting GPU usage:", e)
        return []


class Throttling:
    def __init__(self, retriever, sender=None, timing=1, start_=None):
        self.r = retriever
        self.s = sender
        self.t = timing
        self.n = time()
        self.store = start_

    def update(self):
        t = time() - self.n
        if t > self.t:
            d = self.r()
            if self.s is not None:
                self.s(d)
            self.store = d
            self.n = time()


def end_it():
    x = 0.1
    main_screen.clear()
    graph.clear()
    screen.update()
    sleep(x)
    text.clear()
    screen.update()
    sleep(x)
    turtle.clear()
    screen.update()
    for _ in range(100):
        draw_label('Shutting Down. . .', 'Shutting Down. . .', 0, 50, 0.3, 0)
        screen.update()
        text.clear()
    write_file(0, 'cpu_stop.txt')


def write_file(val, name):
    with open(name, 'w') as file:
        file.write(str(val))
        file.close()


class TargetController:
    def __init__(self, target, transition_time=1.0):
        self.target = target
        self.transition_time = transition_time
        self.output = 0.0
        self.t = 0.0
        self.velocity = 0.0

    def change_target(self, target):
        self.target = remove_decimal(target)
        self.t = 0.0
        self.velocity = 0.0

    def update(self, dt):
        self.t += dt
        if self.t > self.transition_time:
            self.output = self.target
            self.velocity = 0.0
            return

        t = self.t / self.transition_time
        self.output = self.target * t + (1 - t) * self.output
        self.velocity = (self.target - self.output) / dt


def check_saves():
    if not os.path.exists(os.path.join(script_dir, 'cpu_stop.txt')):
        with open(os.path.join(script_dir, 'cpu_stop.txt'), 'w') as file:
            file.write('0')
            file.close()

    if not os.path.exists(os.path.join(script_dir, 'cpu_bridge.txt')):
        with open(os.path.join(script_dir, 'cpu bridge.txt'), 'w') as file:
            file.write('0')
            file.close()


def run_mouse_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()


def on_click(x, y, button, pressed_):
    global pressed, press_check
    if debug:
        print(button)
        print(f"Left mouse button clicked at ({x}, {y})")
    pressed = pressed_


def get_mouse():
    x, y = pyautogui.position()
    window_handle = FindWindow(None, screen_name)
    window_rect = GetWindowRect(window_handle)
    screen_x, screen_y = window_rect[0], window_rect[1]
    turtle_x = (x - screen_x) - 490
    turtle_y = -((y - screen_y) - 440)
    if int(screen.window_width()) != screen_dim[0] or int(screen.window_height()) != screen_dim[1]:
        screen.setup(screen_dim[0], screen_dim[1])
    return turtle_x, turtle_y


class NumberAverager:
    def __init__(self, tim_):
        self.numbers = []
        self.t = tim_

    def add_number(self, num):
        self.numbers.append((num, time()))

    def get_average(self):
        self.remove_old_numbers()
        if not self.numbers:
            return 0
        return sum(num[0] for num in self.numbers) / len(self.numbers)

    def remove_old_numbers(self):
        now = time()
        self.numbers = [(num, timestamp) for (num, timestamp) in self.numbers if now - timestamp <= self.t]


mouse_thread = threading.Thread(target=run_mouse_listener)
mouse_thread.daemon = True
mouse_thread.start()


check_saves()
start()
