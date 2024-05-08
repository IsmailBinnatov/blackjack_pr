# Game Functions

def calculate_points(hand):
    total_points = 0

    for card in hand:
        value = card.split('.')[1]
        if value.isdigit():
            total_points += int(value)
        elif isinstance(value, str):
            total_points += 10
        elif value == 'A':
            total_points += 11

    return total_points

