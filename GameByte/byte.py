import random

import pygame

# Initialize Game
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)

# Initializing the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Even Number Crush")

# Generate even numbers by multiplying 2 by powers of 2
possible_values = [2 ** i for i in range(1, 6)]  # Values: 2, 4, 8, 16, 32

# Create a grid of these numbers
grid = [[random.choice(possible_values) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
selected_candy = None
score = 0

def handle_click(row, col):
    global selected_candy
    if selected_candy is None:
        selected_candy = (row, col)
    else:
        row1, col1 = selected_candy
        grid[row][col], grid[row1][col1] = grid[row1][col1], grid[row][col]
        selected_candy = None

def detect_match():
    matches = set()
    # Horizontal Matches
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 2):
            if grid[row][col] == grid[row][col + 1] == grid[row][col + 2]:
                matches.add((row, col))
                matches.add((row, col + 1))
                matches.add((row, col + 2))
    # Vertical Matches
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 2):
            if grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
                matches.add((row, col))
                matches.add((row + 1, col))
                matches.add((row + 2, col))
    return matches

def fill_empty_spaces():
    for col in range(GRID_SIZE):
        empty_count = sum(1 for row in range(GRID_SIZE) if grid[row][col] == 0)
        for row in range(GRID_SIZE - 1, -1, -1):
            if grid[row][col] == 0:
                for r in range(row, 0, -1):
                    grid[r][col] = grid[r - 1][col]
                grid[0][col] = random.choice(possible_values)

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // CELL_SIZE
            row = event.pos[1] // CELL_SIZE
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                handle_click(row, col)
    
    screen.fill(WHITE)

    # Draw numbers
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            number = grid[row][col]
            number_color = (255, 0, 0) if number == 2 else (0, 255, 0) if number == 4 else (0, 0, 255) if number == 8 else (255, 255, 0) if number == 16 else (0, 255, 255)
            pygame.draw.rect(screen, number_color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            font = pygame.font.SysFont(None, 55)
            img = font.render(str(number), True, (0, 0, 0))
            screen.blit(img, (col * CELL_SIZE + CELL_SIZE // 2 - img.get_width() // 2, row * CELL_SIZE + CELL_SIZE // 2 - img.get_height() // 2))

    matches = detect_match()
    if matches:
        for row, col in matches:
            score += grid[row][col] * 2  # Multiply the score by 2
            grid[row][col] = 0
        fill_empty_spaces()

    # Update the display
    pygame.display.flip()

pygame.quit()
print("Final Score:", score)
