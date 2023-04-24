from lib.report_length import *

def test_report_length_return_12_for_hello_world():
    result = report_length("Hello World.")
    assert result == "This string was 12 characters long."