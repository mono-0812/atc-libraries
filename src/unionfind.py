class unionfind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1 for i in range(self.n)]

    def find(self,x):
        if self.parents[x]<0:
            return x
        self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:return
        if self.size(x)<self.size(y):
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    
    def size(self,x):
        return -self.parents[self.find(x)]
    
    def is_same(self,x,y):
        return int(self.find(x)==self.find(y))



