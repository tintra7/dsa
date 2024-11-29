def rod_cutting(price, n):
    dp = [0] * (n + 1)
    price = [0] + price
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i == 8 and j == 2:
                print(dp[j],  price[i - j])
            dp[i] = max(price[i], dp[j] + price[i - j], dp[i])

    return dp[n]

print(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8))