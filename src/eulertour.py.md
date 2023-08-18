---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/segmenttree.py
    title: src/segmenttree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: eulertour.test.py
    title: eulertour.test.py
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
  code: "from .segmenttree import segmenttree\n\nclass eulertour():\n    def __init__(self,path,s):\n\
    \        self.n=len(path)\n        self.path=path\n        self.used=[0 for i\
    \ in range(self.n)]\n        self.used[s]=1\n        self.tour=[]\n        self._eulertour(s,0)\n\
    \        self.in_index=[10**18]*(self.n)\n        self.out_index=[-10**18]*(self.n)\n\
    \        self.seg=segmenttree([(-1,-1)]*(len(self.tour)),(10**18,-1),lambda x,y:min(x,y))\n\
    \        for i in range(len(self.tour)):\n            depth,v=self.tour[i]\n \
    \           self.seg.update(i,(depth,v))\n            self.in_index[v]=min(i,self.in_index[v])\n\
    \            self.out_index[v]=max(i,self.out_index[v])\n\n    def _eulertour(self,v,depth):\n\
    \        self.tour.append((depth,v))\n        for i in self.path[v]:\n       \
    \     if self.used[i]:continue\n            self.used[i]=1\n            self._eulertour(i,depth+1)\n\
    \            self.tour.append((depth,v))\n\n    def lca(self,u,v):\n        if\
    \ self.in_index[u]>self.in_index[v]:\n            u,v=v,u\n        return self.seg.query(self.in_index[u],self.in_index[v]+1)[1]"
  dependsOn:
  - src/segmenttree.py
  isVerificationFile: false
  path: src/eulertour.py
  requiredBy: []
  timestamp: '2023-08-18 14:44:39+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - eulertour.test.py
documentation_of: src/eulertour.py
layout: document
redirect_from:
- /library/src/eulertour.py
- /library/src/eulertour.py.html
title: src/eulertour.py
---
