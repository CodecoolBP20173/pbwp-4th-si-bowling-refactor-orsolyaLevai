def scoring_when_all_pins_down(game, result, frame, total_frames, max_pins_number, roll_index):
    """
    Scoring when all pins are down and the game isn't in the last round.

    Args:
    game -> string (1-9, x, -, /)
    result -> number
    frame -> number
    total_frames -> number
    max_pins_number -> number
    roll_index -> number

    Return:
    result -> number
    """
    if is_a_spare(game[roll_index]):
        result += get_value(game[roll_index+1])
    elif is_a_strike(game[roll_index]):
        result += get_value(game[roll_index+1])
        if is_a_spare(game[roll_index+2]):
            result += max_pins_number - get_value(game[roll_index+1])
        else:
            result += get_value(game[roll_index+2])
    return result


def set_all_pins_down_in_the_first_roll(in_first_half, frame, current_roll_points):
    """
    Sets the frame number and a bool value.

    Args:
    in_first_half -> bool
    frame -> number
    current_roll_points -> number

    Returns:
    frame -> number
    in_first_half -> bool
    """
    if in_first_half:
        in_first_half = False
    else:
        frame += 1
        in_first_half = True

    if is_a_strike(current_roll_points):
        in_first_half = True
        frame += 1
    return frame, in_first_half


def is_a_score_between_one_and_nine(char):
    """
    Decides the character is a number between 1 and 9.

    Args:
    char -> string

    Returns:
    bool
    """
    return char == '1' or char == '2' or char == '3' or \
        char == '4' or char == '5' or char == '6' or \
        char == '7' or char == '8' or char == '9'


def is_a_strike(char):
    """
    Decides if the character is a strike roll (X or x)

    Args:
    char -> string

    Returns:
    bool
    """
    return char == 'X' or char == 'x'


def is_a_spare(char):
    """
    Decides if the character is a spare frame

    Args:
    char -> string

    Returns:
    bool
    """
    return char == '/'


def is_a_miss(char):
    """
    Decides if the character means "missed"

    Args:
    char -> string

    Returns:
    bool
    """
    return char == '-'


def score(game):
    """
    Control the scoring and shows the result.

    Args:
    game -> string

    Returns:
    result -> number
    """
    result = 0
    frame = 1
    in_first_half = True
    total_frames = 10
    max_pins_number = 10

    for roll_index in range(len(game)):
        if is_a_spare(game[roll_index]):
            result += total_frames - last_frame
        else:
            result += get_value(game[roll_index])

        if frame < total_frames and get_value(game[roll_index]) == max_pins_number:
            result = scoring_when_all_pins_down(game, result, frame, total_frames, max_pins_number, roll_index)

        last_frame = get_value(game[roll_index])
        frame, in_first_half = set_all_pins_down_in_the_first_roll(in_first_half, frame, game[roll_index])

    return result


def get_value(char):
    """
    Gives the score points according to a given character (strike(x, X), spare(/), missed(-), scored (1-9))
    It raises ValueError, if the given character is unknown.

    Args:
    char -> string

    Returns:
    a number
    """
    if is_a_score_between_one_and_nine(char):
        return int(char)
    elif is_a_strike(char):
        return 10
    elif is_a_spare(char):
        return 10
    elif is_a_miss(char):
        return 0
    else:
        raise ValueError()
