import curses
import random


def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(20, 60, 0, 0)
    w.keypad(True)
    w.nodelay(True)
    w.border(0)

    snake = [(10, 30), (10, 29), (10, 28)]
    food = (random.randint(1, 18), random.randint(1, 58))
    w.addch(food[0], food[1], '*')
    score = 0

    key = curses.KEY_RIGHT
    ESC = 27

    while key != ESC:
        w.addstr(0, 2, f'Score: {score} ')
        prev_key = key
        event = w.getch()
        key = event if event != -1 else prev_key

        if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = prev_key

        y = snake[0][0]
        x = snake[0][1]
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_LEFT:
            x -= 1
        if key == curses.KEY_RIGHT:
            x += 1

        snake.insert(0, (y, x))
        if y == 0 or y == 19 or x == 0 or x == 59 or snake[0] in snake[1:]:
            break
        if snake[0] == food:
            score += 1
            food = ()
            while food == () or food in snake:
                food = (random.randint(1, 18), random.randint(1, 58))
            w.addch(food[0], food[1], '*')
        else:
            last = snake.pop()
            w.addch(last[0], last[1], ' ')
        w.addch(snake[0][0], snake[0][1], '#')

    w.nodelay(False)
    w.getch()

curses.wrapper(main)
