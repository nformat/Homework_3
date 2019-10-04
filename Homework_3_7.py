s = ''' We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
'''
print("\nВ тексте", len(s.split()) ,"слов")

s = s.split()
print(s)
bad = ["!", ",", "'", ".", "(", ")"]
f = 0
for i in s:
    for b in bad:
        i = i.strip(b)
    s[f] = i
    f += 1
print("\nСписок без лишних знаков:\n", s)
s.sort()
print("\nОтсортированный список\n", s)


c=0
d= {}
for i in s:
    i = i.lower()
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print("\nСлова в строке встречаются следующее количество раз:\n", d)
