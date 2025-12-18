s = input("Enter a String :")

count = {}
left = 0
right = 0

res = ""

for i,ch in enumerate(s):
    if ch in count:
        left = count[ch]+1
    
    count[ch] = i

    if i - left + 1 > right:
        right = i - left + 1
    res = s[left:i+1]
print(res)