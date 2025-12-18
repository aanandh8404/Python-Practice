# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


l1 = list(map(int,input("Enter l1 values :").split()))
l2 = list(map(int,input("Enter l2 values :").split()))

s1 = ''.join(str(i) for i in l1[::-1])
s2 = ''.join(str(i) for i in l2[::-1])

sum = int(s1) + int(s2)

result = list(map(int,(str(sum)[::-1])))
print(result)