# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

from src.segmenttree import segmenttree

N,Q=map(int,input().split())
a=list(map(int,input().split()))
seg=segmenttree(a,0,lambda x,y:x+y)

for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==0:
        seg.add(query[1],query[2])
    else:
        print(seg.query(query[1],query[2]))
        

