t = int(input())
rslt = ''
for i in range(t):
    r,s = input().split()
    for j in range(len(s)):
        rslt += s[j]*int(r)
    print(rslt)
    rslt = ''