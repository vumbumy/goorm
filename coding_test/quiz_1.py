# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


n = int(input())
layers = [ int(value) for value in input().split() ]

answer = 0

layers_len = len(layers)

for i in range(layers_len - 1):
    answer += layers[i] * layers[i+1]

print(answer)