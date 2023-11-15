class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(string):
            return string == string[::-1]

        longest = ""
        length = len(s)

        for left in range(length):
            for right in range(left + 1, length + 1):
                substring = s[left:right]

                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring

        return longest
