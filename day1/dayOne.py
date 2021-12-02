inputF = open("day1/input.txt", "r")
input = inputF.read().split()
# lastdepth = input[0]
d = 0
lastdepth = 10000
for depth in input:
    c = int(depth)
    if lastdepth < c:
        d += 1
    lastdepth = c
print(d)

l = 10000
dd = 0
for index in range(len(input) - 3):
    c = int(input[index])
    z = int(input[index + 3])
    if c < z:
        dd += 1
print(dd)
