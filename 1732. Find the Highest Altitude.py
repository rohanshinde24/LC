class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n, alt, total, high = len(gain), [0], 0, 0
        for i in range(n):
            total += gain[i]
            alt.append(total)
            if alt[i+1]>high:
                high = alt[i+1]
        # alt = sorted(alt, reverse = True)
        return high