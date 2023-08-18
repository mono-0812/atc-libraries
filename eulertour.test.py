# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca

from src.eulertour import eulertour

import sys
sys.setrecursionlimit(900000)

N,Q=map(int,input().split())
p=list(map(int,input().split()))

path=[[] for i in range(N)]
for i in range(N-1):
    path[i+1].append(p[i])
    path[p[i]].append(i+1)

tour=eulertour(path,0)
for i in range(Q):
    u,v=map(int,input().split())
    print(tour.lca(u,v))
    




