---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: topologicalsort.test.py
    title: topologicalsort.test.py
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
  code: "import collections\n\ndef topologicalsort(path):\n    n=len(path)\n    cnt=[0]*n\n\
    \    for i in range(n):\n        for j in path[i]:\n            cnt[j]+=1\n  \
    \  q=collections.deque([i for i in range(n) if cnt[i]==0])\n    res=[]\n    while\
    \ q:\n        v=q.popleft()\n        res.append(v)\n        for i in path[v]:\n\
    \            cnt[i]-=1\n            if not cnt[i]:\n                q.append(i)\n\
    \n    return res if sum(cnt)==0 else []"
  dependsOn: []
  isVerificationFile: false
  path: src/topologicalsort.py
  requiredBy: []
  timestamp: '2023-08-18 15:17:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - topologicalsort.test.py
documentation_of: src/topologicalsort.py
layout: document
redirect_from:
- /library/src/topologicalsort.py
- /library/src/topologicalsort.py.html
title: src/topologicalsort.py
---
