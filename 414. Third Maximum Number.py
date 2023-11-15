class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniquearr = list(set(nums))
        uniquearr = sorted(uniquearr,reverse=True)
        size = len(uniquearr)
        if size>2:
            return uniquearr[2]
        else:
            return uniquearr[0]