import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.split(r'/+', path)
        res = []
        print(path)
        for item in path:
            if item == ".." and len(res) > 0:
                res.pop()
            else:
                if item != '.':
                    res.append(item)
        return "/".join(res)[:-1]
                
s = Solution()
print(s.simplifyPath(path="/home/user/Documents/../Pictures/"))