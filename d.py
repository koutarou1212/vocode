from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)
for _ in range(M):
    Ai, Bi = map(int, input().split())
    dsu.merge(Ai - 1, Bi - 1)

print(dsu.groups())