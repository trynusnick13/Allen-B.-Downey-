"""

PALINDROME

"""


def palindrome(str):

    if str[0] == str[-1]:

        if len(str) <= 2:

            return True

        else :

          return palindrome(str[1:-1])

    else:

        return False

print(palindrome("abba"))

