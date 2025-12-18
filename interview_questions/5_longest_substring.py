a = input("Enter a string :")

char_index = {}
start = 0
max_len = 0
res = ""

for i,ch in enumerate(a):
    if ch in char_index and char_index[ch] >= start:
        start = char_index[ch] + 1
    
    char_index[ch] = i

    if i - start + 1 > max_len:
        max_len = i - start + 1
        res = a[start:i+1]

print(res)

# def longest_unique_substring(s):
#     char_index = {}
#     start = 0
#     max_len = 0
#     longest_sub = ""

#     for i, ch in enumerate(s):
#         if ch in char_index and char_index[ch] >= start:
#             start = char_index[ch] + 1
        
#         char_index[ch] = i

#         if i - start + 1 > max_len:
#             max_len = i - start + 1
#             longest_sub = s[start:i+1]

#     return longest_sub

# print(longest_unique_substring("abcabcdabc"))
