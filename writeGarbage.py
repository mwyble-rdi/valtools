from random import shuffle
garbagelist = []
for i in range(1,20):
    for g in range(32,126):
        garbagelist.append(chr(g))
        shuffle(garbagelist)

with open("garbagefile.txt", 'w') as f:
    for g in garbagelist:
        f.write(g)