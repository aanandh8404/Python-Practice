def chef_dishes(N,C,A):
    A.sort(key= lambda x:x[1])
    p = C
    count = 0
    for e,m in A:
        if e >= p:
            count += 1
            p = max(p,m)
    return count

def main():
    N = int(input())
    C = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int,input().split(" "))))
    result = chef_dishes(N,C,A)
    print(result)

if __name__ == "__main__":
    main()

# input

# 4
# 5
# 5 5
# 5 5
# 5 5
# 5 5

# output
# 4

# input

# 3
# 3
# 3 7
# 3 6
# 6 8

# output
# 2

# input

# 3
# 5
# 1 7
# 1 6
# 6 8

# output
# 1