# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

from src.fenwicktree import fenwicktree

N,Q=map(int,input().split())
ft=fenwicktree(N)
a=list(map(int,input().split()))

for i in range(N):
    ft.add(i,a[i])

for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==0:
        ft.add(query[1],query[2])
    else:
        print(ft.query(query[1],query[2]))
