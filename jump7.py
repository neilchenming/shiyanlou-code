j=0
for j in range(100):
    j+=1
    if j%7==0 or j%10==7 or j//10==7:
        continue
    else:
      print(j)
