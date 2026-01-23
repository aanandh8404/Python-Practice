class Solution:
    def isPalindrome(self,s):
        rev = ''
        for ch in s:
            rev = ch + rev
        return rev == s

    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1] and j-i+1 > max_len:
                    res = s[i:j+1]
                    max_len = j-i+1

        return res
    

obj = Solution()
ans = obj.longestPalindrome("bababxyz")
print(ans)