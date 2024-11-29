class Solution(object):
    def decodeString(self, s):
        stack = []
        curr_num = 0
        curr_str = ''
        for char in s:
            print(stack)
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_num, curr_str))
                curr_num = 0
                curr_str = ''
            elif char == ']':
                temp_num, temp_string = stack.pop()
                curr_str = temp_string + curr_str * temp_num
            else:
                curr_str += char
        return curr_str

            

s = Solution()
print(s.decodeString(s = "3[ad2[cb]]ef"))