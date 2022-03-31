from math import ceil


def time_calc(workers: int, tasks: int, time: int, overall_time: int) -> int:
    result = 0
    if overall_time > 0:
        if workers * tasks * time > overall_time:
            overall_time_now = (time * tasks) / workers
            overall_time_ceiled = ceil(overall_time_now)
            result = workers
            while overall_time_now > overall_time or overall_time_ceiled >= overall_time:
                result += 1
                overall_time_now = (time * tasks) / result
                overall_time_ceiled = ceil(overall_time_now)
            result -= workers
        else:
            if workers == 0:
                result = 1
    else:
        print('невозможна!')
    return result


if __name__ == "__main__":
    assert time_calc(1, 3, 3, 5) == 2, "Must be 2"
    assert time_calc(2, 500, 100, 101) == 498, "Must be 498"
    assert time_calc(12, 40, 9, 10) == 28, "Must be 28"
    assert time_calc(7, 91, 2, 5) == 39, "Must be 39"

