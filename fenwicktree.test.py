# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum

from src.fenwicktree import fenwicktree

N,Q=map(int,input().split())
ft=fenwicktree(N)
a=list(map(int,input().split()))

for i in range(N):
    ft.add(i,a[i])

for i in range(Q):
    l,r=map(int,input().split())
    print(ft.sum(l,r))
