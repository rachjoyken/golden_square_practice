from lib.check_codeword import *

def test_check_codeword_horse_returns_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
