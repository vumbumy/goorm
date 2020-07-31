import math

num = int(input())

root_n = int(math.sqrt(num))

sum = 0
for i in range(1, root_n + 1):
    if num % i == 0:
        sum += i

        j = int(num / i)
        if i != j:
            sum += j

print(sum)
