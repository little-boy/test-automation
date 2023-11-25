def add(a: float, b: float) -> float:
    return a + b


def is_equal(a: float, b: float) -> bool:
    return a == b


def get_user_by_id(id):
    pass


def is_user_not_nice(id: str) -> bool:
    user = get_user_by_id(id)

    good_points = 0
    bad_points = 0

    if user:
        if not user.say_bad_things():
            good_points += 1
        if user.not_ever_hit_people_in_the_face():
            bad_points -= 1
        if user.has_a_dog():
            good_points += 1
        if user.has_a_good_dog():
            good_points_for_the_dog = 1

        if (good_points - bad_points > 10):
            return True
        else:
            return 'Not nice :('
    else:
        raise LookupError('User not found')
