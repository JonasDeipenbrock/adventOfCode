inputF = open("day2/input2.txt", "r")
input = inputF.read().split("\n")

print(input[:5])

d = 0
h = 0
for c in input:
    cn = c.split()
    if cn[0] == "forward":
        h += int(cn[1])
    elif cn[0] == "down":
        d += int(cn[1])
    else:
        d -= int(cn[1])
print(d, h, d * h)

d = 0
h = 0
a = 0
for c in input:
    cn = c.split()
    if cn[0] == "forward":
        h += int(cn[1])
        d += a * int(cn[1])
    elif cn[0] == "down":
        a += int(cn[1])
    else:
        a -= int(cn[1])
print(d, h, d * h)
