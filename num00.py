#new comment code

f = open('/home/asd/Рабочий стол/Web/new.txt')

s = f.readline()

f.close

l = lmax = 1

for i in range(len(s)-1):
    
    if s[i] == 'A' and s[i+1] == 'A':
       
        l += 1
        lmax = max(l, lmax)

    else:
        
        l = 1

print(lmax)