import pygame
from sudoku import Sudoku

WIDTH, HEIGHT = 665, 912
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# top left of the grid starts at (57, 57)
# each box is 57 x 57 pixels

# logo and title
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(icon)


# background
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
generButton = pygame.transform.scale(pygame.image.load("images/gener.png"), (180, 80))
solveButton = pygame.transform.scale(pygame.image.load("images/solve.png"), (180,80))
checkButton = pygame.transform.scale(pygame.image.load("images/check.png"), (180,80))


# images list
images = [
    pygame.image.load("images/blank.png"),
    pygame.transform.scale(pygame.image.load("images/newOne.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/two.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/three.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/newFour.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/newFive.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/six.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/seven.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/eight.png"), (57,57)),
    pygame.transform.scale(pygame.image.load("images/nine.png"), (57,57)),
    pygame.image.load("images/immutable.png"),
    pygame.image.load("images/standard.png"),
    pygame.image.load("images/error.png")
]


# constants
TILE_SIZE = 57
OFFSET = 19

class MySudoku:
    def __init__(self):
        puzzle = Sudoku(3).difficulty(0.6)
        board = puzzle.board

        self.tiles = [[0 for x in range(9)] for x in range(9)]

        for i in range(9):
            for j in range(9):
                offsetX = i // 3
                offsetY = j // 3

                x = TILE_SIZE + TILE_SIZE * i + offsetX * OFFSET
                y = TILE_SIZE + TILE_SIZE * j + offsetY * OFFSET

                value = board[i][j]
                immutable = True
                if (value == None):
                    value = 0
                    immutable = False

                self.tiles[i][j] = Tile(x, y)
                self.tiles[i][j].val = value
                self.tiles[i][j].immutable = immutable
    
    def update(self):
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].update()

    def solve(self):
        
        find = self.findEmpty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.isValid(i, (row, col)):
                self.tiles[row][col].val = i

                if self.solve():
                    return True

                self.tiles[row][col].val = 0
                

        return False

    # pos is a tuple
    def isValid(self, num, pos):
        # Check row
        for i in range(9):
            if self.tiles[pos[0]][i].val == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if self.tiles[i][pos[1]].val == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.tiles[i][j].val == num and (i,j) != pos:
                    return False

        return True

    def findEmpty(self):
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j].val == 0:
                    return (i, j)  # row, col

        return None


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = 0
        self.image = images[0]
        self.immutable = False
        self.valid = True


    def update(self):
        self.image = images[self.val]

        if (self.immutable):
            WINDOW.blit(images[10], (self.x, self.y))
        elif (self.valid == False):
            WINDOW.blit(images[12], (self.x, self.y))
        else:
            WINDOW.blit(images[11], (self.x, self.y))
        WINDOW.blit(self.image, (self.x, self.y))


def main():
    run = True
    sudoku = MySudoku()
    focused = None

    timer = 0
    started = False

    
    while run:
        
        WINDOW.blit(background, (0, 0))
        WINDOW.blit(checkButton, (45, 675))
        WINDOW.blit(solveButton, (245, 675))
        WINDOW.blit(generButton, (445, 675))
        sudoku.update()


        if (started):
            timer += 1
            if (timer == 80):
                timer = 0
                started = False
                for i in range(9):
                        for j in range(9):
                            sudoku.tiles[i][j].valid = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False        


            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if (675 <= pos[1] <= 755):
                    if (45 < pos[0] <= 225):
                        started = True
                        for i in range(9):
                            for j in range(9):
                                tile = sudoku.tiles[i][j]
                                if (sudoku.isValid(sudoku.tiles[i][j].val, (i, j)) or sudoku.tiles[i][j].val == 0):
                                    sudoku.tiles[i][j].valid = True
                                else: 
                                    sudoku.tiles[i][j].valid = False

                    if (245 <= pos[0] <= 425):
                        sudoku.solve()
                    if (445 <= pos[0] <= 625):
                        sudoku = MySudoku()
                

                for i in range(9):
                    for j in range(9):
                        tile = sudoku.tiles[i][j]

                        if (tile.x < pos[0] < tile.x + TILE_SIZE
                                and tile.y < pos[1] < tile.y + TILE_SIZE):
                                focused = tile
                
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_1 and focused:
                    focused.val = 1
                if event.key == pygame.K_2 and focused:
                    focused.val = 2
                if event.key == pygame.K_3 and focused:
                    focused.val = 3
                if event.key == pygame.K_4 and focused:
                    focused.val = 4
                if event.key == pygame.K_5 and focused:
                    focused.val = 5
                if event.key == pygame.K_6 and focused:
                    focused.val = 6
                if event.key == pygame.K_7 and focused:
                    focused.val = 7
                if event.key == pygame.K_8 and focused:
                    focused.val = 8
                if event.key == pygame.K_9 and focused:
                    focused.val = 9
                if event.key == pygame.K_BACKSPACE:
                    sudoku.solve()

        pygame.display.update()
    pygame.quit()
    

if __name__ == "__main__":
    main()