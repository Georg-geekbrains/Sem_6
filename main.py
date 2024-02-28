
"""
from queens import can_place_queens

test_positions = [
    [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)],  
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],  
]

for i, positions in enumerate(test_positions, start=1):
    if can_place_queens(positions):
        print(f"Тест {i}: Расстановка корректна.")
    else:
        print(f"Тест {i}: Расстановка некорректна.")
"""
"""
from queens import find_successful_queen_positions

successful_positions = find_successful_queen_positions()
for position in successful_positions:
    print(position)
"""


from date_checker import validate_date

print(validate_date('29.02.2000'))  
print(validate_date('29.02.1900'))  