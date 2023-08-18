---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: src/topologicalsort.py
    title: src/topologicalsort.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A\n\
    \nfrom src.topologicalsort import topologicalsort\n\nV,E=map(int,input().split())\n\
    path=[[] for i in range(V)]\n\nfor i in range(E):\n    u,v=map(int,input().split())\n\
    \    path[u].append(v)\n\nprint(int(len(topologicalsort(path))==0))\n\n    \n\
    \        \n\n"
  dependsOn:
  - src/topologicalsort.py
  isVerificationFile: true
  path: topologicalsort.test.py
  requiredBy: []
  timestamp: '2023-08-18 15:17:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: topologicalsort.test.py
layout: document
redirect_from:
- /verify/topologicalsort.test.py
- /verify/topologicalsort.test.py.html
title: topologicalsort.test.py
---
