import pytest
from testbook import testbook


@pytest.fixture(scope="module")
def tb():
    with testbook("./my_story.ipynb", execute=True) as tb:
        yield tb


def test_add(tb):
    add = tb.ref("add")
    assert add(1, 2) == 3
    assert add(2, 3) == 5


def test_print(tb):
    assert tb.cell_output_text(4) == "Hello World"
