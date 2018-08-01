
"""
In MS-Paint, when we take the brush to a pixel and click,
the color of the region of that pixel is replaced with a new selected color.
Following is the problem statement to do this task.
Given a 2D screen, location of a pixel in the screen and a color,
replace color of the given pixel and all adjacent same colored pixels with the
given color.

Author: Narendra L
Date: 21-7-2018
"""

img = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 2, 0],
[1, 0, 0, 1, 0, 2, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[2, 2, 1, 1, 1, 2, 2, 1],
]


lenr = len(img)
lenc = len(img[0])

visited = []


def neighbours(r, c):
    """Calculates the neighbours of a given cell"""
    return [[r+1, c], [r+1, c], [r-1, c], [r, c-1],
            [r+1, c+1], [r+1, c-1], [r-1, c-1], [r-1, c+1]]


def flood_fill(r, c, color, replace_color):
    """Flood fills the given segment starting from given index"""
    if r < 0 or r >= lenr:
        return

    if c < 0 or c >= lenc:
        return

    if img[r][c] != color:
        return

    img[r][c] = replace_color

    visited.append([r, c])

    moves = neighbours(r, c)

    for move in moves:
        if move not in visited:
            flood_fill(move[0], move[1], color, replace_color)


def flood_img():
    print("Input")

    for i in img:print i

    replace_point = (4, 4)
    flood_fill(*replace_point, color=2, replace_color=3)

    print "-" * 25
    print "output"
    for i in img:print i


flood_img()

