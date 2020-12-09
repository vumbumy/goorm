# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = 0
path = []

line_n = 0
last_index = 0

dp = []


def dfs(i, j):
    if i == line_n - 1:
        return path[i][0]

    if dp[i][j] != -1:
        return dp[i][j]

    next_row = len(path[i + 1])

    max_sum = 0
    if i < last_index:
        max_sum = dfs(i + 1, j)
        if j + 1 < next_row:
            max_sum = max(max_sum, dfs(i + 1, j + 1))
    else:
        if j < next_row:
            max_sum = max(max_sum, dfs(i + 1, j))
        if j - 1 >= 0:
            max_sum = max(max_sum, dfs(i + 1, j - 1))

    dp[i][j] = path[i][j] + max_sum

    return dp[i][j]


if __name__ == "__main__":
    n = int(input())

    line_n = 2 * n - 1
    last_index = n - 1

    for _ in range(line_n):
        line = [int(n) for n in input().split()]

        path.append(line)
        dp.append([-1] * len(line))

    print(dfs(0, 0))

