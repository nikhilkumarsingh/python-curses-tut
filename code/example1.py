import time
import curses

# initialize application
stdscr = curses.initscr()

# tweak terminal settings
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

# write something on the screen
stdscr.addstr(5, 10, "Hello, world!")

# update the screen
stdscr.refresh()

# wait for 3 seconds
time.sleep(3)

# clear the screen
stdscr.clear()

# reverse terminal settings
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

# close the application
curses.endwin()