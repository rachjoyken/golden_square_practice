from lib.grammar_stats import *

def test_check_grammar():
    text = GrammarStats()
    assert text.check("Hello!") == True

def test_check_no_grammar():
    text = GrammarStats()
    assert text.check("bye") == False 

def test_percentage():
    text = GrammarStats()
    text.check("Hello!")
    text.check("bye")
    assert text.percentage_good() == 50 

def test_percentage():
    text = GrammarStats()
    text.check("Hello!")
    text.check("bye")
    text.check("HI?")
    text.check("goodbye...")
    text.check("Hey!")
    text.check("byebyebye")
    text.check("HIHI!!")
    assert text.percentage_good() == 57

