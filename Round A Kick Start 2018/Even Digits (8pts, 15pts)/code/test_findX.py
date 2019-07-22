import answer


def test_findX():
    assert answer.findX(23522) == 22888
    assert answer.findX(13000) == 8888
    assert answer.findX(2) == 2
