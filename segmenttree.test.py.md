---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/segmenttree.py
    title: src/segmenttree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    \nfrom src.segmenttree import segmenttree\n\nN,Q=map(int,input().split())\na=list(map(int,input().split()))\n\
    seg=segmenttree(a,0,lambda x,y:x+y)\n\nfor i in range(Q):\n    query=list(map(int,input().split()))\n\
    \    if query[0]==0:\n        seg.add(query[1],query[2])\n    else:\n        print(seg.query(query[1],query[2]))\n\
    \        \n\n"
  dependsOn:
  - src/segmenttree.py
  isVerificationFile: true
  path: segmenttree.test.py
  requiredBy: []
  timestamp: '2023-08-17 20:56:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: segmenttree.test.py
layout: document
redirect_from:
- /verify/segmenttree.test.py
- /verify/segmenttree.test.py.html
title: segmenttree.test.py
---
