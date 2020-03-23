j=0
for j  in range(100):
    j+=1
    if j%7==0:
        continue
    if j%10==7:
        continue
    if j//10==7:
        continue
    print(j)
