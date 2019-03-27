import curses
from curses import textpad


def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.getch()


curses.wrapper(main)