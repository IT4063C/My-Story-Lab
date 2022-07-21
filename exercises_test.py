import pytest
from testbook import testbook


@pytest.fixture(scope="module")
def tb():
    with testbook("./python-exercises.ipynb", execute=True) as tb:
        yield tb


def test_fizzbuzz(tb):
    assert tb.cell_output_text(2) == "Exercise 1"
