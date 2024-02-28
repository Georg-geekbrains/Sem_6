import random

def can_place_queens(positions):
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if positions[i][0] == positions[j][0] or \
               positions[i][1] == positions[j][1] or \
               abs(positions[i][0] - positions[j][0]) == abs(positions[i][1] - positions[j][1]):
                return False
    return True

def generate_random_positions():
    return [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]

def find_successful_queen_positions():
    successful_positions = []

    while len(successful_positions) < 4:
        random_positions = generate_random_positions()
        if can_place_queens(random_positions):
            successful_positions.append(random_positions)

    return successful_positions

