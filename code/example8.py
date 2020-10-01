import random
import curses
from curses import textpad

OPPOSITE_DIRECTION_DICT = {
	curses.KEY_UP: curses.KEY_DOWN,
	curses.KEY_DOWN: curses.KEY_UP,
	curses.KEY_RIGHT: curses.KEY_LEFT,
	curses.KEY_LEFT: curses.KEY_RIGHT
}

DIRECTIONS_LIST = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]

def create_food(snake, box):
	"""Simple function to find coordinates of food which is inside box and not on snake body"""
	food = None
	while food is None:
		food = [random.randint(box[0][0]+1, box[1][0]-1), 
		random.randint(box[0][1]+1, box[1][1]-1)]
		if food in snake:
			food = None
	return food


def main(stdscr):
	# initial settings
	curses.curs_set(0)
	stdscr.nodelay(1)
	stdscr.timeout(100)

	# create a game box
	sh, sw = stdscr.getmaxyx()
	box = [[3,3], [sh-3, sw-3]]  # [[ul_y, ul_x], [dr_y, dr_x]]
	textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
	
	# create snake and set initial direction
	snake = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2-1]]
	direction = curses.KEY_RIGHT

	# draw snake
	for y,x in snake:
		stdscr.addstr(y, x, '#')

	# create food
	food = create_food(snake, box)
	stdscr.addstr(food[0], food[1], '*')

	# print score
	score = 0
	score_text = "Score: {}".format(score)
	stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)

	while 1:
		# non-blocking input
		key = stdscr.getch()
			
		# set direction if user pressed any arrow key and that key is not opposite of current direction
		if key in DIRECTIONS_LIST and key != OPPOSITE_DIRECTION_DICT[direction]:
			direction = key

		# find next position of snake head
		head = snake[0]
		if direction == curses.KEY_RIGHT:
			new_head = [head[0], head[1]+1]
		elif direction == curses.KEY_LEFT:
			new_head = [head[0], head[1]-1]
		elif direction == curses.KEY_DOWN:
			new_head = [head[0]+1, head[1]]
		elif direction == curses.KEY_UP:
			new_head = [head[0]-1, head[1]]

		# insert and print new head
		stdscr.addstr(new_head[0], new_head[1], '#')
		snake.insert(0, new_head)
		
		# if sanke head is on food
		if snake[0] == food:
			# update score
			score += 1
			score_text = "Score: {}".format(score)
			stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
			
			# create new food
			food = create_food(snake, box)
			stdscr.addstr(food[0], food[1], '*')

			# increase speed of game
			stdscr.timeout(100 - (len(snake)//3)%90)
		else:
			# shift snake's tail
			stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
			snake.pop()

		# conditions for game over
		if (snake[0][0] in [box[0][0], box[1][0]] or 
			snake[0][1] in [box[0][1], box[1][1]] or 
			snake[0] in snake[1:]):
			msg = "Game Over!"
			stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
			stdscr.nodelay(0)
			stdscr.getch()
			break

curses.wrapper(main)
