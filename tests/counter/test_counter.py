from src.pre_built.counter import count_ocurrences


def test_counter():
    counter = count_ocurrences("data/jobs.csv", "file")
    assert counter == 306
