class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = ""
        temp = ""
        cnt = 0
        s=s.strip()
        for i in s:
            if i is not " ":
                temp += i
                cnt = 0
            elif i is " ":
                reverse = temp + reverse
                if cnt==0:
                    reverse = " " + reverse
                    cnt += 1
                temp = ""
        reverse = temp + reverse
        return reverse