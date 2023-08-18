---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/eulertour.py
    title: src/eulertour.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\n\nfrom\
    \ src.eulertour import eulertour\n\nimport sys\nsys.setrecursionlimit(900000)\n\
    \nN,Q=map(int,input().split())\np=list(map(int,input().split()))\n\npath=[[] for\
    \ i in range(N)]\nfor i in range(N-1):\n    path[i+1].append(p[i])\n    path[p[i]].append(i+1)\n\
    \ntour=eulertour(path,0)\nfor i in range(Q):\n    u,v=map(int,input().split())\n\
    \    print(tour.lca(u,v))\n    \n\n\n\n\n"
  dependsOn:
  - src/eulertour.py
  isVerificationFile: true
  path: eulertour.test.py
  requiredBy: []
  timestamp: '2023-08-18 14:44:39+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: eulertour.test.py
layout: document
redirect_from:
- /verify/eulertour.test.py
- /verify/eulertour.test.py.html
title: eulertour.test.py
---
