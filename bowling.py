def score(game):
    result = 0
    frame = 1
    in_first_half = True
    total_frames = 10

    for i in range(len(game)):
        if is_a_spare(game[i]):
            result += total_frames - last_frame
        else:
            result += get_value(game[i])

        if frame < total_frames and get_value(game[i]) == 10:
            if is_a_spare(game[i]):
                result += get_value(game[i+1])
            elif is_a_strike(game[i]):
                result += get_value(game[i+1])
                if is_a_spare(game[i+2]):
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last_frame = get_value(game[i])

        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True

        if is_a_strike(game[i]):
            in_first_half = True
            frame += 1

    return result


def get_value(char):
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


def is_a_score_between_one_and_nine(char):
    return char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9'


def is_a_strike(char):
    return char == 'X' or char == 'x'


def is_a_spare(char):
    return char == '/'


def is_a_miss(char):
    return char == '-'
