from typing import List

# def maxProfitHelper(prices, l, r):
#     if l == r:
#         return 0
#     if r == (l + 1):
#         return max(0, prices[r] - prices[l])
#     m = (l + r) // 2
#     m1 = maxProfitHelper(prices, l, m)
#     m2 = maxProfitHelper(prices, m + 1, r)
#     min_left = min(prices[l:m + 1])
#     max_right = max(prices[m: r + 1])
#     return max(m1, m2, max_right-min_left)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))