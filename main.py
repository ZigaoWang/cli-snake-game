import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random

def print_game_over(win):
    win.clear()
    win.addstr(10, 25, 'Game Over!')
    win.refresh()
    curses.napms(2000)

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT
score = 0

snake = [[4,10], [4,9], [4,8]]
food = [10,20]

win.addch(food[0], food[1], curses.ACS_PI)

while key != 27:
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    speed = 150 - (len(snake)) // 5 + len(snake) // 10 % 120
    win.timeout(speed)

    prevKey = key
    event = win.getch()
    key = key if event == -1 else event

    if key == ord(' '):
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = prevKey

    y = snake[0][0]
    x = snake[0][1]
    if key == KEY_DOWN:
        y += 1
    if key == KEY_UP:
        y -= 1
    if key == KEY_LEFT:
        x -= 1
    if key == KEY_RIGHT:
        x += 1

    snake.insert(0, [y, x])

    if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59 or snake[0] in snake[1:]:
        print_game_over(win)
        break

    if snake[0] == food:
        score += 1
        food = []
        while food == []:
            food = [random.randint(1, 18), random.randint(1, 58)]
            if food in snake:
                food = []
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print(f"Final score = {score}")
