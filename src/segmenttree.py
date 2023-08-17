class segmenttree():
    def __init__(self,init_sequence,identify,operator):
        self.n=len(init_sequence)
        self.tree=[identify]*(self.n*2)
        self.op=operator
        self.ide=identify

        for i, x in enumerate(init_sequence, self.n):
            self.tree[i] = x
            
        for i in range(self.n)[::-1]:
            self.tree[i]=operator(self.tree[i<<1],self.tree[i<<1|1])

    def update(self,i,x):
        i+=self.n
        self.tree[i]=x
        while i>1:
            i>>=1
            self.tree[i]=self.op(self.tree[i<<1],self.tree[i<<1|1])
    
    def add(self,i,x):
        self.update(i,self.tree[i+self.n]+x)

    def query(self,l,r):
        l+=self.n
        r+=self.n
        l_value,r_value=self.ide,self.ide

        while l<r:
            if l&1:
                l_value=self.op(l_value,self.tree[l])
                l+=1

            if r&1:
                r-=1
                r_value=self.op(self.tree[r],r_value)
            
            l>>=1
            r>>=1
        
        return self.op(l_value,r_value)