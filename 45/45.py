from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10e5] * n
        dp[0] = 0
        for i in range(1, n):
            min_step = 10e4
            for j in range(0, i):
                if nums[j] >= (i - j) and dp[j] < min_step:
                    min_step = dp[j]

            dp[i] = min_step + 1
        return dp[-1]

s = Solution()
print(s.jump(nums = [2,3,1,1,4]))