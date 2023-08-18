---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/fenwicktree.py
    title: src/fenwicktree.py
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
    \nfrom src.fenwicktree import fenwicktree\n\nN,Q=map(int,input().split())\nft=fenwicktree(N)\n\
    a=list(map(int,input().split()))\n\nfor i in range(N):\n    ft.add(i,a[i])\n\n\
    for i in range(Q):\n    query=list(map(int,input().split()))\n    if query[0]==0:\n\
    \        ft.add(query[1],query[2])\n    else:\n        print(ft.query(query[1],query[2]))\n"
  dependsOn:
  - src/fenwicktree.py
  isVerificationFile: true
  path: fenwicktree.test.py
  requiredBy: []
  timestamp: '2023-08-17 20:56:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: fenwicktree.test.py
layout: document
redirect_from:
- /verify/fenwicktree.test.py
- /verify/fenwicktree.test.py.html
title: fenwicktree.test.py
---
