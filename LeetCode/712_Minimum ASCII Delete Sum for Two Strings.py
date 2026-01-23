def minimumDeleteSum( s1: str, s2: str):
        s1 = sorted(s1)
        s2 = sorted(s2)
        sum = 0
        for i in s1:
            if i not in s2:
                s1.remove(i)
                sum += ord(i)
        
        for i in s2:
            if i not in s1:
                s2.remove(i)
                sum += ord(i)

        return sum
        

print(minimumDeleteSum('delete','leet'))