---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: fenwicktree.test.py
    title: fenwicktree.test.py
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
  code: "class fenwicktree():\n    def __init__(self,n):\n        self.n=n\n     \
    \   self.bit_length=len(bin(n))-2\n        self.tree=[0]*(n+1)\n\n    #i\u306B\
    x\u3092\u52A0\u7B97 0-indexed\n    def add(self,i,x):\n        i+=1\n        while\
    \ i<=self.n:\n            self.tree[i]+=x\n            i+=i&-i\n    \n    def\
    \ _sum(self,i):\n        if i<0:return 0\n        if i>self.n:i=self.n\n     \
    \   res=0\n        while i>0:\n            res+=self.tree[i]\n            i-=i&-i\n\
    \        return res\n    \n    #[l,r)\u306E\u548C 0-indexed\n    def query(self,l,r):\n\
    \        l+=1\n        return self._sum(r)-self._sum(l-1)\n    \n    def bisect_left(self,x):\n\
    \        if x==0:return 0\n        res=0\n        for i in range(self.bit_length)[::-1]:\n\
    \            if (1<<i)|res>self.n:continue\n            if x>self.tree[(1<<i)|res]:\n\
    \                x-=self.tree[(1<<i)|res]\n                res|=(1<<i)\n     \
    \   return res+1\n    \n    def bisect_right(self,x):\n        res=0\n       \
    \ for i in range(self.bit_length)[::-1]:\n            if (1<<i)|res>self.n:continue\n\
    \            if x>=self.tree[(1<<i)|res]:\n                x-=self.tree[(1<<i)|res]\n\
    \                res|=(1<<i)\n        return res+(x!=0)\n        "
  dependsOn: []
  isVerificationFile: false
  path: src/fenwicktree.py
  requiredBy: []
  timestamp: '2023-08-17 20:56:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - fenwicktree.test.py
documentation_of: src/fenwicktree.py
layout: document
redirect_from:
- /library/src/fenwicktree.py
- /library/src/fenwicktree.py.html
title: src/fenwicktree.py
---
