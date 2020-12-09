# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

team = map(int, input().split())
vuno = map(int, input().split())

vuno = sorted(vuno)

answer = 0

for t in team:
    for v in vuno:
        if t <= v:
            answer += 1
            vuno.remove(v)
            break

print(answer)
