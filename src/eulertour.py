from .segmenttree import segmenttree

class eulertour():
    def __init__(self,path,s):
        self.n=len(path)
        self.path=path
        self.used=[0 for i in range(self.n)]
        self.used[s]=1
        self.tour=[]
        self._eulertour(s,0)
        self.in_index=[10**18]*(self.n)
        self.out_index=[-10**18]*(self.n)
        self.seg=segmenttree([(-1,-1)]*(len(self.tour)),(10**18,-1),lambda x,y:min(x,y))
        for i in range(len(self.tour)):
            depth,v=self.tour[i]
            self.seg.update(i,(depth,v))
            self.in_index[v]=min(i,self.in_index[v])
            self.out_index[v]=max(i,self.out_index[v])

    def _eulertour(self,v,depth):
        self.tour.append((depth,v))
        for i in self.path[v]:
            if self.used[i]:continue
            self.used[i]=1
            self._eulertour(i,depth+1)
            self.tour.append((depth,v))

    def lca(self,u,v):
        if self.in_index[u]>self.in_index[v]:
            u,v=v,u
        try:
            return self.seg.query(self.in_index[u],self.in_index[v]+1)[1]
        except:
            print(self.in_index[u],self.in_index[v]+1)