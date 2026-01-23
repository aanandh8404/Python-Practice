from collections import defaultdict
def minWindow(s, t):
        min_len = float('inf')
        start = 0
        l = r = 0
        n = len(s)

        count = 0

        hash = {}
        for ch in t:
            if ch in hash:
                hash[ch] += 1
            else:
                hash[ch] = 1
        
        for r in range(n):
            if s[r] in hash:
                if hash[s[r]] > 0:
                    count += 1
                hash[s[r]] -= 1

            while count == len(t):
                if r+1 - l < min_len:
                    min_len = r+1 - l
                    start = l
                if s[l] in hash:
                    hash[s[l]] += 1
                    if hash[s[l]]>0:
                        count -= 1
                l += 1

        res = '' if min_len == float('inf') else s[start:start+min_len]
                
        return res

s = "bba"
t = "ab"

print(minWindow(s,t))






        # min_len = 0
        # start = 0
        # n = len(s)
        # for i in range(n):
        #     count = 0
        #     t_count = {}
        #     for ch in t:
        #         if ch not in t_count:
        #             t_count[ch] = 1
        #         else:
        #             t_count[ch] += 1

        #     for j in range(i,n):
        #         if s[j] in t_count and t_count[s[j]] > 0:
        #             t_count[s[j]] -= 1
        #             count += 1
                
        #         if count == len(t):
        #             if j+1 - i < min_len or min_len == 0:
        #                 min_len = j+1 - i
        #                 start = i
        #                 break
        # res = s[start:start+min_len]


            
        # return res