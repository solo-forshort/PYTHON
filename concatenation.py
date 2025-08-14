
def is_palindrome(word):
    return word == word[::-1]
print("...Palindrome checker...")
new_word = input("Enter or Type your word: ")
print(is_palindrome(new_word))
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))