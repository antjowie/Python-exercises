def draw_board(rows,columns):
    for row in range(rows):
        print(' ---' * columns)
        print('|   '*(columns +1))
    print(' ---' * columns)


rows = int(input('How many rows should the board have? '))
columns = int(input('How many columns should the board have? '))

draw_board(rows,columns)