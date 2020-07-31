import math

num = int(input())

if num == 1:
    print("1 ")

    exit(0)

root_n = int(math.sqrt(num))

a = '1'
b = str(num)
for i in range(2, root_n + 1):
    if num % i == 0:
        a = "%s %d" % (a, i)

        if i != num / i:
            b = "%d %s" % (num / i, b)

print("%s %s " % (a, b))
