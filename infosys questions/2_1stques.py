import math
A = [5,3,7,4,9]
N = len(A)
m = 3

max_sum = -1

for i in range(N-m+1):
    for j in range(N-m+1,N+1):
        curr_sub = A[i:j]
        isPassed = False

        gcd = curr_sub[0]
        for num in range(1,len(curr_sub)-1):
            gcd = math.gcd(gcd,curr_sub[num])
        
        harm_sum = 0
        for num in curr_sub:
            harm_sum += 1/num
        harm_mean = len(curr_sub)/harm_sum

        ascend = 1
        curr_num = curr_sub[0]
        for num in curr_sub:
            if num > curr_num:
                ascend += 1
                curr_num = num

        if len(curr_sub) >= 3 and gcd == 1 and harm_mean >= 2 and ascend >= 3:
            isPassed = True

        if isPassed:
            curr_sum = sum(curr_sub)
            max_sum = max(max_sum,curr_sum)

print(max_sum)