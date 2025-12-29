# 1

# nums = list(map(int,input("Enter values of array :").split()))
# target = int(input("Enter target value :"))

# def combination(arr, r, start=0, curr = []):
#     if len(curr) == r:
#         return [curr]
    
#     res = []
#     for i in range(start, len(arr)):
#         res += combination(arr, r, i+1, curr +[arr[i]])
#     return res

# result = combination(nums,4)

# for i in result:
#     if sum(i) == target:
#         print(sorted(i))



# 2

# rows = int(input("Enter number of rows :"))

# for i in range(1,rows+1):

#     for space in range(rows-i,0,-1):
#         print(end=" ")

#     num = 1
#     for j in range(1,i+1):
#         print(num, end=" ")
#         num = int(num * (i-j)/j)

#     print()



# 3

# rows, cols = map(int,input("Enter the number of rows and columns :").split())
# matrix = [[0]*cols for _ in range(rows)]

# num = 1
# top, left = 0,0
# bottom, right = rows-1 , cols-1

# while top <= bottom and left <= right:

#     for i in range(left, right + 1):
#         matrix[top][i] = num
#         num += 1
#     top += 1

#     for i in range(top, bottom + 1):
#         matrix[i][right] = num
#         num += 1
#     right -= 1

#     for i in range(right,left - 1,-1):
#         matrix[bottom][i] = num
#         num += 1
#     bottom -= 1

#     for i in range(bottom, top - 1,-1):
#         matrix[i][left] = num
#         num += 1
#     left += 1

# for i in matrix:
#     print(i)



# 4

# str = input("Enter a String :")
# ch_index = {}
# max_len = 0
# start = 0
# res = ""
# for i,ch in enumerate(str):
#     if ch in ch_index and ch_index[ch] >= start:
#         start = ch_index[ch] + 1
    
#     ch_index[ch] = i

#     if i - start + 1 > max_len:
#         max_len = i - start + 1
#         res = str[start:i+1]

# print(res)


# 5

# s = input("Enter a string :")
# rows = int(input("Enter number of rows :"))
# res = [""]*rows
# r = 0
# down = True
# for i in s:
#     res[r] += i

#     if down:
#         r += 1
#     else:
#         r-=1
    
#     if r == 0:
#         down = True
#     elif r == rows-1:
#         down = False

# print("".join(res))



# 6
# n = int(input("Enter a number :"))

# a, b = 0,1
# result = []

# for i in range(n):
#     is_prime = True
#     if a <= 1:
#         is_prime = False
#     for j in range(2,int(a**0.5)+1):
#         if a%j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         result.append(a)
#     a,b = b, a+b

# print(result)







# tic tac toe

# board = [" "]*9
# current = "X"

# def show():
#     print()
#     print(board[0], "|", board[1], "|", board[2])
#     print("--+---+--")
#     print(board[3], "|", board[4], "|", board[5])
#     print("--+---+--")
#     print(board[6], "|", board[7], "|", board[8])
#     print()

# def check(player):
#     wins = [
#         [0,1,2], [3,4,5], [6,7,8],
#         [0,3,6], [1,4,7], [2,5,8],
#         [0,4,8], [2,4,6]
#     ]

#     return any(board[a] == board[b] == board[c] == player for a,b,c in wins )

# for i in range(9):

#     show()
#     pos = int(input(f"Player {current}, Enter Your position(1 to 9) :")) - 1

#     if board[pos] != " ":
#         print("Invalid position")
#         break

#     board[pos] = current

#     if check(current):
#         show()
#         print(f"{current} Won !!")
#         break
#     current = "O" if current == "X" else "X"

# else:
#     show()
#     print("Draw")

    


# lst = [i**2 if i%2==0 else i**3 for i in range(1,11)]
# print(lst)


# a = 5
# b = 10

# def dec(func):
#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# @dec
# def div(a,b):
#     print(a/b)

# div(a,b)



# num = [12,43, 5,3,12,43]

# res = []

# for i in num:
#     if i in res:
#         continue
#     res.append(i)
# print(res)



# def pal(x):
#     num = x
#     rev = 0
#     while num != 0:
#         rev = rev * 10 + num % 10
#         num //= 10
#     return x == rev

# a = pal(-525)
# print(a)



# def removeDuplicates(nums):
#         res = []
#         for i in nums:
#             if i in res:
#                 continue
#             res.append(i)
#         return res


# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))




def removeElement( nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[k] == val:
                  nums.remove(nums[k])
            else:
                  k += 1
        return nums

print(removeElement([0,1,2,2,3,0,4,2],2))