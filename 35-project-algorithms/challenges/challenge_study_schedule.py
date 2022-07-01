def study_schedule(permanence_period, target_time=None):
    result = 0
    if target_time is None:
        return None
    for entry_time, departure_time in permanence_period:
        if (
            isinstance(entry_time, int)
            and isinstance(departure_time, int)
        ):
            if entry_time <= target_time <= departure_time:
                result += 1
        else:
            return None
    return result

# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 4))
# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 3))
# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1))
# print(study_schedule([(4, None), ("0", 4)], 4))
# print(study_schedule([("A", 9), (None, 5)], 4))
# print(study_schedule([(1, 5), (2, 4), (3, 3), (4, 4), (5, 5)]))
