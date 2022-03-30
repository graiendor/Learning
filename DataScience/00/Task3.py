def TimeCalc(workers, tasks, time, overall_time):
    result = 0
    if overall_time > 0:
        if workers * tasks * time > overall_time:
            required_time = time * tasks
            overall_time_now = workers * time
            result = workers
            while overall_time_now < required_time:
                result += 1
                required_time = time * tasks
                overall_time_now = result * time
            result -= workers
        else:
            if workers == 0:
                result = 1
    else:
        print('невозможна!')
    return result


if __name__ == "__main__":
    # w = 2
    # tk = 500
    # tm = 100
    # otm = 101
    w = 1
    tk = 3
    tm = 3
    otm = 5
    print(TimeCalc(w, tk, tm, otm))
