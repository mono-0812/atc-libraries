class fenwicktree():
    def __init__(self,n):
        self.n=n
        self.bit_length=len(bin(n))-2
        self.tree=[0]*(n+1)

    #iにxを加算 0-indexed
    def add(self,i,x):
        i+=1
        while i<=self.n:
            self.tree[i]+=x
            i+=i&-i
    
    def _sum(self,i):
        if i<0:return 0
        if i>self.n:i=self.n
        res=0
        while i>0:
            res+=self.tree[i]
            i-=i&-i
        return res
    
    #[l,r)の和 0-indexed
    def sum(self,l,r):
        l+=1
        return self._sum(r)-self._sum(l-1)
    
    def bisect_left(self,x):
        if x==0:return 0
        res=0
        for i in range(self.bit_length)[::-1]:
            if (1<<i)|res>self.n:continue
            if x>self.tree[(1<<i)|res]:
                x-=self.tree[(1<<i)|res]
                res|=(1<<i)
        return res+1
    
    def bisect_right(self,x):
        res=0
        for i in range(self.bit_length)[::-1]:
            if (1<<i)|res>self.n:continue
            if x>=self.tree[(1<<i)|res]:
                x-=self.tree[(1<<i)|res]
                res|=(1<<i)
        return res+(x!=0)
        