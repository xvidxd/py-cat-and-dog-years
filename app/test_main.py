import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "first_year,second_year,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15 , 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "0, 0 cat and dog years should be equal to [0, 0]",
        "14, 14 cat and dog years should be equal to [0, 0]",
        "15, 15 cat and dog years should be equal to [1, 1]",
        "23, 23 cat and dog years should be equal to [1, 1]",
        "24, 24 cat and dog years should be equal to [2, 2]",
        "27, 27 cat and dog years should be equal to [2, 2]",
        "28, 28 cat and dog years should be equal to [3, 2]",
        "100, 100 cat and dog years should be equal to [21, 17]",
    ]
)
def test_get_human_age(first_year: int,
                       second_year: int,
                       result: list[int]) -> None:
    assert get_human_age(first_year, second_year) == result
