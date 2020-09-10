import color_stuff
from colr import Colr as C
import turtle as t
import random
import tkinter as tk
from PIL import Image, EpsImagePlugin
from pathlib import Path
import os
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.52\bin\gswin64c'


def get_color_console():
    # input
    artist = input("Enter an artist: ")
    song = input("Enter a song/album by them: ")
    # grab colors
    colors = color_stuff.compute_top_image_colors(song + ' - ' + artist)
    # print colors
    for i, color in enumerate(colors):
        print(C().b_rgb(0, 0, 0).rgb(color[0], color[1], color[2], 'Top color ' + str(i + 1)))


# same as above but no console
def get_colors():
    artist = input("Enter an artist: ")
    song = input("Enter a song/album by them: ")
    colors = color_stuff.compute_top_image_colors(song + ' - ' + artist)
    return {'artist': artist, 'song': song, 'colors': colors}


# gets the length of each line drawn in the diagonal_stripes function
def determine_line_lengths(colors):
    lengths = []
    distance = 100
    for c in colors:
        lengths.append(distance)
        distance += 25
    return lengths



# was a test to make a polygon with n colors sides
def polygon(artist, song, colors):
    t.colormode(255)
    t.title("polygon of " + song + " by " + artist)
    t.speed(1)
    t.pensize(10)
    n = len(colors)
    degrees = 180 * (n-2)
    # how much to rotate each time
    rotate = 180 - degrees/n
    for c in colors:
        t.pencolor(c[0], c[1], c[2])
        t.rt(rotate)
        t.forward(100)
    t.mainloop()


# draws a kind of triangle with the top colors as stripes
def diagonal_stripes(artist, song, colors):
    SPEED = 10  # speed of drawing
    PENSIZE = 10  # size of each line
    LINE_GAP = 35  # gap in between
    STYLE = ('Times New Roman', 10)
    t.hideturtle()  # dont show the turtle
    t.colormode(255)
    t.title(song + " - " + artist)
    t.speed(SPEED)
    t.pensize(PENSIZE)
    t.setposition(0, 0)
    lengths = determine_line_lengths(colors)[::-1]  # makes it look better by reversing the list
    pos = 0
    colors = reversed(colors)
    for i, c in enumerate(colors):
        pos += LINE_GAP
        t.rt(315)  # 45 degree angle to rotate
        # THIS IS FOR THE TEXT UNDER THE IMAGE JUST UNCOMMENT COMMENT IF WANTED
        if not i:
            t.penup()
            t.setposition(0, -25)
            t.write(song + ' - ' + artist, font=STYLE)
            t.setposition(0, 0)
        t.pendown()
        t.pencolor(c[0], c[1], c[2])
        t.forward(lengths[i])
        t.penup()
        t.setposition(0, 0)
        t.rt(45)
        t.forward(pos)
    # smake image and save it
    ts = t.getscreen()
    f = Path('imgs/' + str(song + '_' + artist))
    ts.getcanvas().postscript(file=Path(str(f) + ".eps"))
    img = Image.open(Path(str(f) + ".eps"))
    img.save(Path(str(f) + ".png"), 'png')
    t.mainloop()


# main func
def main():
    # split data up and pass into diagonal_stripes
    data = get_colors()
    artist = data['artist']
    song = data['song']
    colors = data['colors']
    print(colors)
    diagonal_stripes(artist, song, colors)


# call (only runs in terminal really)
if __name__ == "__main__":
    try:
        main()
    finally:
        # remove the .eps files and keep .png ones
        path = Path(Path.cwd() / "imgs")
        for f in os.listdir(path):
            if ".eps" in f:
                os.remove(Path(path / f))
