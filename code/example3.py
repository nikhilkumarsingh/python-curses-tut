import time
import curses

def main(stdscr):
	# turn off cursor blinking
	curses.curs_set(0)

	# get height and width of screen
	h, w = stdscr.getmaxyx()

	# create a new color scheme
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

	# text to be written in center
	text = "Hello, world!"

	# find coordinates for centered text
	x = w//2 - len(text)//2
	y = h//2

	# set color scheme
	stdscr.attron(curses.color_pair(1))

	# write text on screen
	stdscr.addstr(y, x, text)

	# unset color scheme
	stdscr.attroff(curses.color_pair(1))

	# update the screen
	stdscr.refresh()

	# wait for 3 sec before exit
	time.sleep(3)


curses.wrapper(main)