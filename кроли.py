mounth, pairs = [int(x) for x in input().split()]
razm = 1
rost = [0, 0, 0]
rost[2] = pairs
for i in range(mounth - 1):
    rost[0] = rost[1]
    rost[1] = rost[2]
    razm += rost[0]
    rost[2] = razm * pairs
print(razm)
