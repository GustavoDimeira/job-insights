from src.pre_built.counter import count_ocurrences


def test_counter():
    counter = count_ocurrences("tests/counter/fileToRead.txt", "ipsum")
    assert counter == 7
