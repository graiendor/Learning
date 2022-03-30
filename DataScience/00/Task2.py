MetricType = {'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1}
MetricCompare = {'w': 5, 'd': 4, 'h': 3, 'm': 2, 's': 1}


def time_metric_down(time, metric, metric_down):
    try:
        assert MetricCompare.get(metric) > MetricCompare.get(metric_down)
        time = MetricType.get(metric) * time
        time = time / MetricType.get(metric_down)
    except AssertionError:
        print("Ты не оч")
    return time


if __name__ == "__main__":
    time_res = time_metric_down(10, 'm', 's')
    print(time_res)
