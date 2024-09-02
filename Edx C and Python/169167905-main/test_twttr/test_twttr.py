# def main():
#     word = input("Input: ")
#     print(shorten(word))
#     return 0
# def shorten(word):
#     word_copy = ''
#     for i in word:
#         if i.lower() in 'aeiou':
#             continue
#         else:
#             word_copy +=i
#     word = word_copy
#     return word
# if __name__ == "__main__":
#     main()
from twttr import shorten

def test_shorten():
    # Test with a word containing only vowels
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    # Test with a word containing no vowels
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("BCDFGHJKLMNPQRSTVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"
    # Test with a mix of vowels and consonants
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hello World") == "Hll Wrld"
    # Test with empty string
    assert shorten("") == ""
    # Test with numbers and punctuation
    assert shorten("12345") == "12345"
    assert shorten("hello123") == "hll123"
    assert shorten("hello!") == "hll!"
    assert shorten("AEIOUaeiou!") == "!"
    # Test with mixed case and spaces
    assert shorten("TwItTeR is Awesome") == "TwtTR s wsm"

if __name__ == "__main__":
    test_shorten()
