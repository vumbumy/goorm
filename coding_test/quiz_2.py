# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

answer = 0

for i in range(1, n + 1):
    while i > 0:
        v = i % 10

        if v == 3 or v == 6 or v == 9:
            answer += 1

        i = int(i / 10)

print(answer)

