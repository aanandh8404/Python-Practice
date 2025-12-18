s = input("Enter a string :")

stack = []
brackets = ["(",")","{","}","[","]"]
balanced = True

for ch in s:
    if ch in brackets:
        stack.append(ch)

# print(stack)

changed = True
while len(stack) > 1 and changed:
    changed = False
    for i,ch in enumerate(stack):
        # print(ch,i)
        if ch == "(" and stack[i+1] == ")":
                stack.remove(stack[i+1])
                stack.remove(stack[i])
                changed = True   
        if ch == "{" and stack[i+1] == "}":
                stack.remove(stack[i+1])
                stack.remove(stack[i])
                changed = True
        if ch == "[" and stack[i+1] == "]":
                stack.remove(stack[i+1])
                stack.remove(stack[i])
                changed = True
                
# print(stack)
if len(stack) == 0:
    balanced = True
else:
    balanced = False

print(balanced)




# method 2

# s = input("Enter a string :")

# stack = []
# pairs = {
#     ")":"(",
#     "}":"{",
#     "]":"["
# }

# balanced = True

# for ch in s:
#     if ch in pairs.values():
#         stack.append(ch)

#     elif ch in pairs.keys():
#         if not stack:
#             balanced = False
#             break

#         top = stack.pop()
#         if top != pairs[ch]:
#             balanced = False
#             break

# if stack:
#      balanced = False

# print(balanced)