from lib.d2ex_vowel_remover import *

# def test_simple():
#     remover = VowelRemover("ab")
#     result_no_vowels = remover.remove_vowels()
#     assert result_no_vowels == "b"

# def test_long_sentence_with_punctuation():
#     remover = VowelRemover("We will remove the vowels from this sentence.")
#     result_no_vowels = remover.remove_vowels()
#     assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_remove_all_vowels():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""    

#create a class instance to test on the main method lib file, create a break in the 'gutter' early on in the method and step-through. drag a few of the blocks of code to 'watch' to see how they specifically change as the loop is run 
# -> we added an 'else:' + new indented line with 'i +=1' as if not, for e.g. the 'a' was being removed, 'e' becomes the 0th index, and 'i' is the 1st and therefore it's 'i' that's checked next in the loop, skipping 'e' - adding the else, makes sure that the loop goes through every single letter until the conditions can't be met.
