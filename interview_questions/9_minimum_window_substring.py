s = input("Enter the string :")
t = input("Enter the target string :")

t_count = {}

for ch in t:
    if ch not in t_count:
        t_count[ch] = 1
    else:
        t_count[ch] += 1

result = []
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        temp = s[i:j]
        check = True
        for ch in t:
            if ch not in temp:
                check = False
                break
        if check :
            result.append(temp)

res = ""
for i in result:
    flag = False
    for ch in i:
        if ch in t_count:
            if i.count(ch) == t_count[ch]:
                flag = True
            else :
                flag = False
                break
    
    if flag:
        if len(i) < len(res) or res == "":
            res = i

print(res)
