import pygame

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's Game of Life")

# Initialize the grid with all dead cells
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Function to draw the grid
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to get the count of live neighbors
def count_neighbors(x, y):
    count = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx] == 1:
                count += 1
    return count

# Main game loop
drawing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            cell_x = x // CELL_SIZE
            cell_y = y // CELL_SIZE
            if 0 <= cell_x < GRID_WIDTH and 0 <= cell_y < GRID_HEIGHT:
                drawing = True
                grid[cell_y][cell_x] = 1

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = pygame.mouse.get_pos()
                cell_x = x // CELL_SIZE
                cell_y = y // CELL_SIZE
                if 0 <= cell_x < GRID_WIDTH and 0 <= cell_y < GRID_HEIGHT:
                    grid[cell_y][cell_x] = 1

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            new_grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    neighbors = count_neighbors(x, y)
                    if grid[y][x] == 1:
                        if neighbors < 2 or neighbors > 3:
                            new_grid[y][x] = 0
                        else:
                            new_grid[y][x] = 1
                    else:
                        if neighbors == 3:
                            new_grid[y][x] = 1

            grid = new_grid

    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()

pygame.quit()
