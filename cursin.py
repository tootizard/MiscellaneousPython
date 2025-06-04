#!/bin/python3

from time import sleep
import curses

def main(stdscr):
    stdscr.addstr('Lines: {}, Columns: {}'.format(curses.LINES, curses.COLS))
    stdscr.addstr('\nTest')
    stdscr.refresh()
    sleep(5)

curses.wrapper(main)
