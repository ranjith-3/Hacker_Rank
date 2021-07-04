n = int(input())
arr = map(int, input().split())
arr = list(set(arr))
maxval = secmax = -101

for num in arr:
    if num > secmax:
        if num > maxval:
            secmax = maxval
            maxval = num
        elif num < maxval: 
            secmax = num
print(secmax)
