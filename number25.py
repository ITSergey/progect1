
for x in range(174457, 174505):
    n = 0
    a = ''
    for i in range(2, x):
        if x%i == 0:
            n+=1
            a+=' ' + str(i)
    if n == 2:
        print(a)

