---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: segmenttree.test.py
    title: segmenttree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class segmenttree():\n    def __init__(self,init_sequence,identify,operator):\n\
    \        self.n=len(init_sequence)\n        self.tree=[identify]*(self.n*2)\n\
    \        self.op=operator\n        self.ide=identify\n\n        for i, x in enumerate(init_sequence,\
    \ self.n):\n            self.tree[i] = x\n            \n        for i in range(self.n)[::-1]:\n\
    \            self.tree[i]=operator(self.tree[i<<1],self.tree[i<<1|1])\n\n    def\
    \ update(self,i,x):\n        i+=self.n\n        self.tree[i]=x\n        while\
    \ i>1:\n            i>>=1\n            self.tree[i]=self.op(self.tree[i<<1],self.tree[i<<1|1])\n\
    \    \n    def add(self,i,x):\n        self.update(i,self.tree[i+self.n]+x)\n\n\
    \    def query(self,l,r):\n        l+=self.n\n        r+=self.n\n        l_value,r_value=self.ide,self.ide\n\
    \n        while l<r:\n            if l&1:\n                l_value=self.op(l_value,self.tree[l])\n\
    \                l+=1\n\n            if r&1:\n                r-=1\n         \
    \       r_value=self.op(self.tree[r],r_value)\n            \n            l>>=1\n\
    \            r>>=1\n        \n        return self.op(l_value,r_value)"
  dependsOn: []
  isVerificationFile: false
  path: src/segmenttree.py
  requiredBy: []
  timestamp: '2023-08-17 20:56:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - segmenttree.test.py
documentation_of: src/segmenttree.py
layout: document
redirect_from:
- /library/src/segmenttree.py
- /library/src/segmenttree.py.html
title: src/segmenttree.py
---
