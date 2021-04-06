# import re

# def palindromeCheck(text):

#     pattern = re.compile(r'[^a-zA-Z0-9]')
#     text = re.sub(pattern, '', text).upper()
#     print(text)
#     print(text[::-1])

#     if text == text[::-1]:
#         return 'Congrats, this is a palindrome.'
#     else:
#         return 'Sorry! Try again'

# text = input('Type in your palindrome: ')

# print(palindromeCheck(text))


def palindromeChecker(str):
    # print str
    if (len(str) == 2) and (str[0] == str[1]):
        return True
    if len(str) == 1:
        return True
    else:
        return (str[0] == str[-1]) and palindromeChecker(str[1:-1])

print(palindromeChecker('ab'))