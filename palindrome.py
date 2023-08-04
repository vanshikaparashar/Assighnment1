def palindrome(s):
    return s == s[::-1]


word = input("Enter a string: ")

if palindrome(word):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    