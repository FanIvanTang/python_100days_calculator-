from main import add, subtract, multiply, divide


def test_case_add():

    assert [add(1, 3), add(1.30, 0), add(-0.12, 3)] == [1 + 3, 1.30 + 0, -0.12 + 3]


def test_case_sutract():

    assert [subtract(1, 2), subtract(0.32, 4793.13), subtract(-93, -100)] == [
        1 - 2,
        0.32 - 4793.13,
        -93 - (-100),
    ]
