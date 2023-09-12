
def print_screen(screen: list):
    print('\nPantalla Tetris:\n')
    for row in screen:
        print(''.join(map(str, row)))