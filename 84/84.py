from typing import List

def previous_smaller_element(arr):
    pse = []
    st = []
    for i in range(len(arr)):
        while st and st[-1][0] > arr[i]:
            st.pop()

        if not st:
            pse.append(-1)
        else:
            pse.append(st[-1][1])

        st.append((arr[i], i))
    return pse

def next_smaller_element(arr):
    n = len(arr)
    stack = []  # Stack to store indices of elements
    nse = [n] * n  # Array to store the results, initialized with -1
 
    # Iterate through each element in the array
    for i in range(n):
        next_val = arr[i]
 
        # Pop elements from the stack and update results for elements with smaller neighbors
        while len(stack) > 0 and arr[stack[-1]] > next_val:
            nse[stack.pop()] = i
 
        # Push the current index onto the stack
        stack.append(i)
    return nse

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = previous_smaller_element(heights)
        nse = next_smaller_element(heights)

        max_area = max(heights)
        print(pse)
        print(nse)
        for i in range(n):
            L = i - pse[i] - 1
            R = nse[i] - i - 1
            
            max_area = max(max_area, (L + R + 1) * heights[i])
            

        return max_area

s = Solution()
print(s.largestRectangleArea([2,1,2]))

# 1 - (-1) - 1 3 - 1 - -1 