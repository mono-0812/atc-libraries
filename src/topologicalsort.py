import collections

def topologicalsort(path):
    n=len(path)
    cnt=[0]*n
    for i in range(n):
        for j in path[i]:
            cnt[j]+=1
    q=collections.deque([i for i in range(n) if cnt[i]==0])
    res=[]
    while q:
        v=q.popleft()
        res.append(v)
        for i in path[v]:
            cnt[i]-=1
            if not cnt[i]:
                q.append(i)

    return res if sum(cnt)==0 else []