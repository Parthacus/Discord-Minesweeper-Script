import random
arr = []
x = int(input("use preset easy(0), medium(1), difficult(2), insane(3) or pick custom(4): "))
if x == 0:
    n = 5
    b = 5
elif x == 1:
    n = 7
    b = 12
elif x == 2:
    n = 10
    b = 20
elif x == 3:
    n = 10
    b = 100
elif x == 4:
    n = int(input("Enter square size: "))
    b = int(input("Enter number of bombs: "))

for i in range(n):
    new = []
    for x in range(n):
        new.append(0)
    arr.append(new)

while b > 0:
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    arr[x][y] = "X"
    b -= 1

for x in range(n):
    for y in range(n):
        if arr[x][y] != "X":
            t = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if x + dx >= 0 and y + dy >= 0:
                        try:
                            if arr[x+dx][y+dy] == "X": t+=1
                        except: pass
            arr[x][y] = t

f_s = ""
for y in range(n):
    for x in range(n):
        emoji = ""
        b = arr[x][y]
        if b == "X": emoji = "bomb"
        if b == 0: emoji = "white_large_square"
        if b == 1: emoji = "one"
        if b == 2: emoji ="two"
        if b == 3: emoji ="three"
        if b == 4: emoji ="four"
        if b == 5: emoji ="five"
        if b == 6: emoji ="six"
        if b == 7: emoji ="seven"
        if b == 8: emoji ="eight"
        f_s += "||:{}:||".format(emoji)
    f_s += "\n"

print(f_s)
