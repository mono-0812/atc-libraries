# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from src.unionfind import unionfind
import sys

sys.setrecursionlimit(900000)

N,Q=map(int,input().split())
uf=unionfind(N)
for i in range(Q):
    t,u,v=map(int,input().split())
    if t==0:
        uf.union(u,v)
    if t==1:
        print(uf.is_same(u,v))
