# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import queue

n, k = (0, 0)

if __name__ == "__main__":
    n, k = (int(i) for i in input().split())

    dp = [100001] * 100001

    q = queue.Queue()

    q.put((n, 0))
    while not q.empty():
        p, t = q.get()

        if p == k:
            dp[k] = min(dp[k], t)
            continue

        if dp[p] <= t or dp[k] <= t + 1:
            continue

        dp[p] = t

        if p + 1 <= 100000:
            q.put((p + 1, t + 1))
        if p - 1 >= 0:
            q.put((p - 1, t + 1))
        if p * 2 <= 100000:
            q.put((p * 2, t + 1))

    print(dp[k])