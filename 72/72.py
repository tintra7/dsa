# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         word1 = "#" + word1
#         word2 = '#' + word2
#         n = len(word1)
#         m = len(word2)
#         dis = [[float("inf")] * (m) for i in range(n)]
#         dis[0][0] = 0
#         for i in range(1, n):
#             dis[i][0] = i
#         for i in range(1, m):
#             dis[0][i] = i
#         for i in range(1,n):
#             for j in range(1,m):
#                 if word1[i] == word2[j]:
#                     dis[i][j] = dis[i - 1][j - 1]
#                 else:
#                     dis[i][j] = min(dis[i - 1][j], dis[i][j - 1], dis[i-1][j-1]) + 1
#         for i in dis:
#             print(i)
#         return int(dis[-1][-1]) 

# s = Solution()
# print(s.minDistance(word1 = "horse", word2 = "ros"))


def edit_distance_with_backtrace(s1, s2):
    """
    Computes the edit distance between two strings and backtraces the operations.
    
    :param s1: The first string.
    :param s2: The second string.
    :return: A tuple containing the edit distance and the sequence of operations.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    operations = [[None] * (n + 1) for _ in range(m + 1)]

    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = i
        operations[i][0] = "delete"
    for j in range(n + 1):
        dp[0][j] = j
        operations[0][j] = "insert"

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                operations[i][j] = "match"
            else:
                insert_cost = dp[i][j - 1] + 1
                delete_cost = dp[i - 1][j] + 1
                substitute_cost = dp[i - 1][j - 1] + 1

                dp[i][j] = min(insert_cost, delete_cost, substitute_cost)
                if dp[i][j] == substitute_cost:
                    operations[i][j] = "substitute"
                elif dp[i][j] == delete_cost:
                    operations[i][j] = "delete"
                else:
                    operations[i][j] = "insert"

    # Backtrace to find the sequence of operations
    for i in operations:
        print(i)
    i, j = m, n
    sequence = []
    while i > 0 or j > 0:
        op = operations[i][j]
        if op == "match" or op == "substitute":
            sequence.append((op, s1[i - 1], s2[j - 1]))
            i -= 1
            j -= 1
        elif op == "delete":
            sequence.append((op, s1[i - 1], None))
            i -= 1
        elif op == "insert":
            sequence.append((op, None, s2[j - 1]))
            j -= 1

    sequence.reverse()
    return dp[m][n], sequence


# Example Usage
s1 = "kitten"
s2 = "sitting"

distance, ops = edit_distance_with_backtrace(s1, s2)
print(f"Edit Distance: {distance}")
print("Operations:")
for op in ops:
    print(op)
