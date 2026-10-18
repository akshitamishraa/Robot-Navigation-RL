
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Grid settings
ROWS = 10
COLS = 10
CELL_SIZE = 60
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREEN = (0, 200, 0)
YELLOW = (255, 220, 0)
BLUE = (0, 100, 255)
GRAY = (180, 180, 180)

# Start and goal
start = (0, 0)
goal = (9, 9)

# Obstacles: same as training notebook
obstacles = [
    (1, 2), (2, 2), (3, 2),
    (4, 4), (4, 5), (4, 6),
    (6, 3), (7, 3), (8, 3),
    (7, 7), (7, 8)
]

# Actions: Up, Down, Left, Right
actions = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1)
}

# Load trained Q-table
try:
    Q = np.load("q_table.npy")
    print("Q-table loaded successfully!")
    print("Q-table shape:", Q.shape)
except Exception as error:
    print("Error loading q_table.npy:", error)
    pygame.quit()
    sys.exit()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Navigation using Q-Learning")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)


def get_next_position(state, action):
    row, col = state
    dr, dc = actions[action]

    new_row = row + dr
    new_col = col + dc

    if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
        return state

    if (new_row, new_col) in obstacles:
        return state

    return (new_row, new_col)


def get_robot_path():
    path = [start]
    state = start
    visited = {start}

    for _ in range(ROWS * COLS * 4):
        if state == goal:
            return path, True

        # Choose actions in descending Q-value order
        row, col = state
        action_order = np.argsort(Q[row, col])[::-1]

        moved = False

        for action in action_order:
            next_state = get_next_position(state, int(action))

            if next_state != state and next_state not in visited:
                state = next_state
                path.append(state)
                visited.add(state)
                moved = True
                break

        if not moved:
            break

    return path, state == goal


path, goal_reached = get_robot_path()
print("Path:", path)
print("Goal Reached:", goal_reached)

robot_index = 0
last_move_time = 0
running = True


def draw_grid():
    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            if (row, col) in obstacles:
                pygame.draw.rect(screen, BLACK, rect)
            elif (row, col) == start:
                pygame.draw.rect(screen, GREEN, rect)
            elif (row, col) == goal:
                pygame.draw.rect(screen, YELLOW, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

            pygame.draw.rect(screen, GRAY, rect, 1)

    # Draw robot
    current_position = path[robot_index]
    row, col = current_position

    center = (
        col * CELL_SIZE + CELL_SIZE // 2,
        row * CELL_SIZE + CELL_SIZE // 2
    )

    pygame.draw.circle(screen, BLUE, center, CELL_SIZE // 4)

    if robot_index == len(path) - 1:
        message = "Goal Reached!" if goal_reached else "Path Incomplete"
        color = GREEN if goal_reached else (200, 0, 0)
        text = font.render(message, True, color)
        screen.blit(text, (10, 10))

    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                robot_index = 0
                last_move_time = pygame.time.get_ticks()

    current_time = pygame.time.get_ticks()

    if (
        robot_index < len(path) - 1
        and current_time - last_move_time >= 350
    ):
        robot_index += 1
        last_move_time = current_time

    draw_grid()
    clock.tick(60)

pygame.quit()
sys.exit()

