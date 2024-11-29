from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(i) for i in nums]
        str_nums.sort(reverse=True)
        res = ""
        for i in str_nums:
            res += i
        return res

s = Solution()
print(s.largestNumber(nums = [3,30,34,5,9]))
