---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: unionfind.test.py
    title: unionfind.test.py
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
  code: "class unionfind():\n    def __init__(self,n):\n        self.n=n\n       \
    \ self.parents=[-1 for i in range(self.n)]\n\n    def find(self,x):\n        if\
    \ self.parents[x]<0:\n            return x\n        self.parents[x]=self.find(self.parents[x])\n\
    \        return self.parents[x]\n    \n    def union(self,x,y):\n        x=self.find(x)\n\
    \        y=self.find(y)\n        if x==y:return\n        if self.size(x)<self.size(y):\n\
    \            x,y=y,x\n        self.parents[x]+=self.parents[y]\n        self.parents[y]=x\n\
    \    \n    def size(self,x):\n        return -self.parents[self.find(x)]\n   \
    \ \n    def is_same(self,x,y):\n        return int(self.find(x)==self.find(y))\n\
    \n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: src/unionfind.py
  requiredBy: []
  timestamp: '2023-08-17 01:35:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - unionfind.test.py
documentation_of: src/unionfind.py
layout: document
redirect_from:
- /library/src/unionfind.py
- /library/src/unionfind.py.html
title: src/unionfind.py
---
