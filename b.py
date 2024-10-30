A, B, K = map(int, input().split())
print([i for i in range(1, max(A, B) + 1) if A % i == 0 and B % i == 0][-K])