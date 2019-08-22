MIN_SCORE = 0
MAX_SCORE = 100

score = float(input("Enter score: "))


def score_convert(score_value):
    """ Takes a score value and returns in terms of a grade
    90% or higher --> Excellent score
    50% or higher --> Passable score
    under 50%     --> Bad Score
    """
    if score_value < MIN_SCORE or score_value > MAX_SCORE:
        return "Invalid Score!"
    elif score_value >= 90:
        return "Excellent score!"
    elif score_value >= 50:
        return "Passable score!"
    else:
        return "Bad Score!"


print(score_convert(score))
