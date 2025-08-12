from easy.missingNumber import missingNumber

def test_missingNumber():
    assert missingNumber([0, 3, 1]) == 2
    assert missingNumber([1, 0]) == 2
    assert missingNumber([6, 9, 2, 4, 5, 3, 1, 7, 0]) == 8