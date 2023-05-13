import random
import curses

screen = curses.initscr()

curses.curs_set(False)

screen_h = screen.getmaxyx()[0]
screen_w = screen.getmaxyx()[1]

windows = curses.newwin(screen_h, screen_w, 0, 0)

windows.keypad(True)

windows.timeout(150)

snake_y = screen_h // 2
snake_x = screen_w // 4

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

apple = [screen_h // 2, screen_w // 2]

windows.addch(apple[0], apple[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = windows.getch()

    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, screen_h] or snake[0][1] in [0, screen_w] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    if snake[0] == apple:
        apple = None

        while apple is None:

            new_apple = [
                random.randint(1, screen_h-1),
                random.randint(1, screen_w-1)
            ]

            apple = new_apple if new_apple not in snake else None

        windows.addch(apple[0], apple[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        windows.addch(tail[0], tail[1], ' ')

    windows.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
