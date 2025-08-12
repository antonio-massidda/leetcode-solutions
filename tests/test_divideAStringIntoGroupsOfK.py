from easy.divideAStringIntoGroupsOfK import divideString

def test_divideString():
    assert divideString("cbaedfihg", 3, "x") == ['cba', 'edf', 'ihg']
    assert divideString("cbaedfihgj", 3, "x") == ['cba', 'edf', 'ihg', 'jxx']