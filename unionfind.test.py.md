---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/unionfind.py
    title: src/unionfind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nfrom src.unionfind import unionfind\nimport sys\n\nsys.setrecursionlimit(900000)\n\
    \nN,Q=map(int,input().split())\nuf=unionfind(N)\nfor i in range(Q):\n    t,u,v=map(int,input().split())\n\
    \    if t==0:\n        uf.union(u,v)\n    if t==1:\n        print(uf.is_same(u,v))\n"
  dependsOn:
  - src/unionfind.py
  isVerificationFile: true
  path: unionfind.test.py
  requiredBy: []
  timestamp: '2023-08-17 01:35:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: unionfind.test.py
layout: document
redirect_from:
- /verify/unionfind.test.py
- /verify/unionfind.test.py.html
title: unionfind.test.py
---
