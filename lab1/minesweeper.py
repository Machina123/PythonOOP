import random
def get_number(a,b,text):
    """ Pobiera i zwraca liczbę całkowitą z zakresu <a; b> """
    while True:
        try:
            data = input(f"{text} (liczba z zakresu {a} do {b}): ")
            number = int(data)
        except ValueError:
            print(f"{data} to nie jest liczba")
        else:
            if a <= number <= b:
                return number
            else:
                print(f"{number} jest poza zakresem")

def lay_mines(number_of_mines, rows, cols):
    """ Zwraca zbiór przechowujący współrzędne min """
    mines = set()
    while len(mines) < number_of_mines:
        m = random.randrange(rows)
        n = random.randrange(cols)
        mines.add((m,n))
    return mines


def neighbouring(field, mines, rows, cols):
    """ Zwraca liczbę min sąsiadujących z danym polem (field) """
    i = field[0]
    j = field[1]
    mine_count = 0
    potential_neighbours = [(i-1,j-1), (i-1,j), (i-1,j+1),
                            (i,j-1), (i, j+1),
                            (i+1, j-1), (i+1,j), (i+1, j+1)]

    for m,n in potential_neighbours:
        if 0 <= m < rows and 0 <= n < cols and (m,n) in mines:
            mine_count += 1
    return mine_count

def gen_board(rows, cols, mines, mine = 'x'):
    """ Generuje planszę do gry w sapera """
    board = []
    for i in range(rows):
        line = []
        for j in range(cols):
            if (i,j) in mines:
                line.append(mine)
            else:
                line.append(neighbouring((i,j), mines, rows, cols))
        board.append(line)
    return board

def reveal(board, field, rows, cols, revealed):
    """ Odkrywa pola """
    i = field[0]
    j = field[1]
    potential_neighbours = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                            (i, j - 1), (i, j + 1),
                            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    if not (0 <= i < rows and 0 <= j < cols) or (i,j) in revealed:
        return
    revealed.add((i,j))
    if board[i][j] != 0:
        return
    for m,n in potential_neighbours:
        reveal(board, (m,n), rows, cols, revealed)

def play():
    width = 10
    height = 10
    no_mines = 10
    mines = lay_mines(width, height, no_mines)
    board = gen_board(width, height, mines)
    for line in board:
        for elem in line:
            print(f"{elem:^3}", end='')
        print("")

play()