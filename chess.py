white_horizon = int(input('white horizon position: '))
white_vertical = int(input('white vertical position: '))
black_horizon = int(input('black horizon position: '))
black_vertical = int(input('black vertical position: '))
white_move_horizon = int(input('white move horizon: '))
white_move_vertical = int(input('white move vertical: '))
which_figure = input('which figure is white')

# ладья
if which_figure == 'rook':
    if black_horizon == white_move_horizon and black_vertical == white_move_vertical:
        print('white rook can not move')
    else:
        print('white rook can move')

# слон
if which_figure == 'bishop':
    if abs(black_horizon - white_move_horizon) == abs(black_vertical - white_move_vertical):
        print('white bishop can not move')
    else:
        print('white bishop can move')

# король
if which_figure == 'king':
    if abs(black_horizon - white_move_horizon) == 1 or abs(black_vertical - white_move_vertical) == 1:
        print('white king can not move')
    else:
        print('white king can move')

# ферзь
if which_figure == 'queen':
    if abs(black_horizon - white_move_horizon) == abs(black_vertical - white_move_vertical) \
            or black_horizon == white_move_horizon or black_vertical == white_move_vertical:
        print('white queen can not move')
    else:
        print('white queen can move')

# конь
if which_figure == 'knight':
    if abs(abs(black_vertical - white_move_vertical) - 1) < 0.5 or abs(abs(black_vertical - white_move_vertical) - 2)<0.5:
        print('white knight can not move')
    else:
        print('white knight can move')
