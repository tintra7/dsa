# def check_palindrome(s):
#     return s == s[::-1]


# class Solution:
#     def shortestPalindrome(self, s: str, count=0) -> str:
#         dic = set(s)
#         print(s)
#         if check_palindrome(s):
#             return s
#         for i in dic:
#             return self.shortestPalindrome(i + s)

# s = Solution()
# print(s.shortestPalindrome(s = "aacecaaa"))

def check_palindrome(s):
    return s == s[::-1]


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        # Find the longest palindromic prefix
        for i in range(n + 1):
            if s.startswith(rev_s[i:]):
                # Add the remaining part of the reverse string to the start
                return rev_s[:i] + s
        return s  # Should never reach here


s = Solution()
print(s.shortestPalindrome(s="aacecaaa"))
