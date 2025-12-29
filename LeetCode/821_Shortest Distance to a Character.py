# def shortestToChar(s, c):
#         res = []
#         current_index = s.index(c)
#         for i, ch in enumerate(s):
            
#             if ch == c:
#                 current_index = i
#             a = abs(current_index - i)
#             res.append(a)
#         return res

# print(shortestToChar("loveleetcode","e"))


def shortestToChar(s, c):
        res = []
        current_index = s.index(c)
        for i in range(len(s)):
            
            if s[i] == c:
                current_index = i
            a = abs(current_index - i)
            res.append(a)
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                current_index = i
            res[i] = min(res[i],abs(current_index-i))

        return res

print(shortestToChar("loveleetcode","e"))




















# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         n = len(s)
#         res = [n] * n
        
#         # Left to right
#         prev = -n
#         for i in range(n):
#             if s[i] == c:
#                 prev = i
#             res[i] = i - prev
        
#         # Right to left
#         prev = 2 * n
#         for i in range(n - 1, -1, -1):
#             if s[i] == c:
#                 prev = i
#             res[i] = min(res[i], prev - i)
        
#         return res
