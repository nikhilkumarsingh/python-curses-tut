import curses


def main(stdscr):

	while 1:
		key = stdscr.getch()

		# clear existing texts
		stdscr.clear()

		if key == curses.KEY_UP:
			stdscr.addstr(0, 0, "You pressed Up key!")
		elif key == curses.KEY_DOWN:
			stdscr.addstr(0, 0, "You pressed Down key!")
		elif key == curses.KEY_ENTER or key in [10, 13]:
			stdscr.addstr(0, 0, "You pressed Enter.")
		else:
			break

		# update screen
		stdscr.refresh()


curses.wrapper(main)