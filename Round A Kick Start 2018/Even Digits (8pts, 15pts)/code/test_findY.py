import answer


def test_findY():
    assert answer.findY(86912) == 88000
    assert answer.findY(6488962) == 6600000
    assert answer.findY(88892) == 200000
    assert answer.findY(91112) == 200000
    assert answer.findY(2) == 2
