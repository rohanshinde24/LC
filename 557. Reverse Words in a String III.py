class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ''
        new = ''
        for i in s:
            if i is not ' ':
                temp = i + temp
            if i is ' ':
                new += temp + i
                temp = ''
        return new + temp