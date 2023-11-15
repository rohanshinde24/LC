class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}
        count_set = set()

        for num in arr:
            count_dict[num] = count_dict.get(num, 0) + 1

        for count in count_dict.values():
            if count in count_set:
                return False
            count_set.add(count)

        return True
       