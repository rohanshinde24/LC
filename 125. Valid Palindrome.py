class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        s = str.lower(s)
        for i in s:
            if i.isalnum():
                new += i
        return new == new[::-1]