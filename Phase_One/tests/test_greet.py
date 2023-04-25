from lib.greet import *

def test_greet_returns_hello_rachel():
    result = greet("Rachel")
    assert result == "Hello, Rachel!"