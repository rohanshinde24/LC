class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        
        num_times_won = 0
        first = arr[0]
        
        for num in arr[1:]:
            if num > first:
                num_times_won = 1
                first = num
            else:
                num_times_won += 1
            
            if num_times_won == k:
                return first
        
        return first 