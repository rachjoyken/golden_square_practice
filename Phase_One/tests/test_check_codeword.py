from lib.check_codeword import *

def test_check_codeword_horse_returns_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_house_return_close():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_foal_return_incorrect():
    result = check_codeword("foal")
    assert result == "WRONG!"    