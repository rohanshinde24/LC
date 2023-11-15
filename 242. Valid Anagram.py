class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) > len(t) or len(s) > len(t)):
            return False
        table = defaultdict(int)
        for i in s:
            table[i] += 1
        for i in t:
            table[i] -= 1
        for i in table.values():
            if i != 0:
                return False
        return True