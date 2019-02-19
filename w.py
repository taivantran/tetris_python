import sys
import os
import curses
from random import randint
import time


def del_element(e, lst):
    kq = []
    for i in range(len(lst)):
        if lst[i][0] == e:
            kq.append(i)
    count = 0
    for i in kq:
        del lst[i - count]
        count += 1
    return lst


def check_horizontal(leng, lst):
    for i in range(len(lst)-1):
        dem = 0
        for j in range(len(lst)):
            if lst[i][0] == lst[j][0]:
                dem += 1
        if dem == leng:
            return lst[i][0]
    return None


def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    stdscr.timeout(10)
    score = 0
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    kq = []
    # Loop where k is the last character pressed
    while (k != ord('q')):
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        # add border
        for i in range(height):
            stdscr.addstr(i, width//2, '#')
        # draw score
        stdscr.addstr(cursor_y, cursor_x, 'X')
        stdscr.addstr(height//2, width//2 + 20, str(score))
        if kq != []:
            index = check_horizontal(width//2, kq)
            if index is not None:
                kq = del_element(index, kq)
                for i in range(len(kq)):
                    kq[i][0] = kq[i][0] + 1
                score += 1
        for i in kq:
            stdscr.addstr(i[0], i[1], 'X')
        if k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        else:
            if cursor_y < height - 1 and [cursor_y, cursor_x] not in kq:
                cursor_y = cursor_y + 1
            else:
                if [cursor_y, cursor_x] not in kq:
                    kq.append([cursor_y, cursor_x])
                else:
                    kq.append([cursor_y - 1, cursor_x])
                cursor_y = 0
                # cursor_x = randint(0, width//2 -1)
        cursor_x = max(0, cursor_x)
        cursor_x = min(width//2-1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)
        stdscr.addstr(height-1, width//2 + 1, "Press 'q' to exit",
                      curses.color_pair(3))
        stdscr.addstr(height//2, width//2 + 10, 'score: ')
        # Render border
        start_x_border = (width // 2)
        stdscr.move(cursor_y, cursor_x)
        # Refresh the screen
        stdscr.refresh()
        k = stdscr.getch()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
