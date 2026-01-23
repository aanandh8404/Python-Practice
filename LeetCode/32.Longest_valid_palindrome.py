def longestValidParentheses(s):
        stack = [-1]   # base index
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)   # reset base
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
        # max_len = 0
        # start = 0
        # end = 1
        # stack = []
        # if len(s) == 1:
        #     return max_len
        # for i in range(len(s)):
        #     if start < end:
        #         if s[i] == ')' and not stack:
        #             stack.append(s[i])
        #             start = i + 1
        #             end = start + 1
        #             # max_len -= 1

        #         elif s[i] == ')' and stack.pop() == '(':
        #             end += 1

        #         elif s[i] == '(':
        #             stack.append(s[i])

        #         # if s[i] == "(" and s[i+1] != ")":
        #             # start = i + 1
        #             # max_len -= 1

        #         else:
        #             start += 1
            
        #     max_len = max(max_len,end+1 - start)
            

        # max_len -= len(stack)
        # return max_len

s = "((()))"

print(longestValidParentheses(s))