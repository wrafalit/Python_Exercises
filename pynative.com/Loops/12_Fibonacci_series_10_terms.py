fibunaci = [0,1]
n = 10
for i in range(n+1):
    if i > 2:
        fibunaci.append(fibunaci[i-3] + fibunaci[i-2])
print(fibunaci)
