class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSum = nums[0]
        maxSum = nums[0]
        for n in nums[1:]:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)

        return max(maxSum, currSum)