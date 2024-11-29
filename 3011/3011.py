from typing import List

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def list_segment(nums):
    res = [[nums[0]]]
    last_set_bit = count_set_bits(nums[0])
    for i in range(1, len(nums)):
        current_set_bit = count_set_bits(nums[i])
        if current_set_bit == last_set_bit:
            res[-1].append(nums[i])
        else:
            res.append([nums[i]])
            last_set_bit = current_set_bit
    return res
        


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        segment_list = list_segment(nums)
        for i in range(len(segment_list) - 1):
            if max(segment_list[i]) > min(segment_list[i+1]):
                return False
        return True



s = Solution()
print(s.canSortArray(nums = [3,16,8,4,2]))