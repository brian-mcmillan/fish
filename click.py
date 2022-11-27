from board import TILES


def on_click(event):
    """Purpose: 1. Wait for click and retrieve the x,y coordinates of a given click
                2. Call is_inside_hexagon(), which checks to see if given click is inside any valid hexagon
       Contract: click -> x,y coordinate"""
    global x, y
    x = event.x
    y = event.y
    is_inside_hexagon()



def find_area(x1, y1, x2, y2, x3, y3):
    """Purpose: Helper --> "Returns area of a triangle
       Contract: triangle coordinates -> area"""

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def is_inside_rectangle(bottom_left_x, bottom_right_x, bottom_y, top_y):
    """Purpose: Check if x and y of any click are inside the inner rectangle of a hexagon
       Contract: coordinates -> boolean"""

    # Checks if point is in inner rectangle
    if bottom_left_x < x < bottom_right_x and bottom_y < y < top_y:
        return True
    else:
        return False


def is_inside_left(bottom_left_x, bottom_left_y, mid_left_x, mid_left_y, top_left_x, top_left_y):
    """Purpose: Check if x and y of any click are inside the left triangle of a hexagon
       Contract: coordinates -> boolean"""

    # AREA OF TRIANGLE ABC
    left_area = find_area(bottom_left_x, bottom_left_y, mid_left_x, mid_left_y, top_left_x, top_left_y)

    # AREA OF TRIANGLE PBC
    left_area2 = find_area(x, y, mid_left_x, mid_left_y, top_left_x, top_left_y)

    # AREA OF TRIANGLE APC
    left_area3 = find_area(bottom_left_x, bottom_left_y, x, y, top_left_x, top_left_y)

    # AREA OF TRIANGLE ABP
    left_area4 = find_area(bottom_left_x, bottom_left_y, mid_left_x, mid_left_y, x, y)

    # Check if point is inside left-side triangle
    if left_area == (left_area2 + left_area3 + left_area4):
        return True
    else:
        return False


def is_inside_right(bottom_right_x, bottom_right_y, mid_right_x, mid_right_y, top_right_x, top_right_y):
    """Purpose: Check if x and y of any click are inside the right triangle of a hexagon
       Contract: coordinates -> boolean"""

    # AREA OF TRIANGLE ABC
    right_area = find_area(bottom_right_x, bottom_right_y, mid_right_x, mid_right_y, top_right_x, top_right_y)

    # AREA OF TRIANGLE PBC
    right_area2 = find_area(x, y, mid_right_x, mid_right_y, top_right_x, top_right_y)

    # AREA OF TRIANGLE APC
    right_area3 = find_area(bottom_right_x, bottom_right_y, x, y, top_right_x, top_right_y)

    # AREA OF TRIANGLE ABP
    right_area4 = find_area(bottom_right_x, bottom_right_y, mid_right_x, mid_right_y, x, y)

    # Check if point is in right-side triangle
    if right_area == (right_area2 + right_area3 + right_area4):
        return True
    else:
        return False


def is_inside_hexagon():
    global clicked_hexagon_key
    """Purpose: call is_inside_rectangle, is_inside_left, is_inside_right and pass the coordinates
       of every valid hexagon on the grid. If any return True, the click is valid.
       Contract: dictionary of coordinates -> boolean"""
    # Iterate through each value in dictionary of GRID POSITION: COORDINATES
    for value in TILES.values():
        true_count = 0
        # Check if click is inside the inner rectangle of any valid hexagon
        if is_inside_rectangle(value[0], value[2], value[1], value[9]):
            print(True)
            true_count += 1

        # Checks if click is inside the left triangle of any valid hexagon
        if is_inside_left(value[0], value[1], value[10], value[11], value[8], value[9]):
            print(True)
            true_count += 1

        # Checks if click is inside the right triangle of any valid hexagon
        if is_inside_right(value[2], value[3], value[4], value[5], value[6], value[7]):
            print(True)
            true_count += 1


        if true_count > 0:
            clicked_hexagon_key = {i for i in TILES if TILES[i] == value}

            clicked_hexagon_value = value

            print(clicked_hexagon_key)








