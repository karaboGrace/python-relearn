#learned about break and contunue in loops
for i in range(5):
    if i == 3:
        break
    print(i)
#output 0,1,2   stops completely at i=3

for i in range(5):
    if i == 3:
        continue
    print(i)
#output 0,1,2,4   skips only 3 