N, M = map(int, input().split())
A = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
for I in map(list, zip(A, *X)):
    if I[0] >= sum(I[1:]):
        print("No")
        exit()
print("Yes")