# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B&lang=jp

from src.topologicalsort import topologicalsort

V,E=map(int,input().split())
path=[[] for i in range(V)]

for i in range(E):
    u,v=map(int,input().split())
    path[u].append(v)

print(*topologicalsort(path))
        

