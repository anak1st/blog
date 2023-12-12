---
title: Disjoint Set Union
date: 2023-03-10 16:18:12
updated: 2023-03-10 16:18:12
tags:
categories:
- [templates, data structure]
keywords:
description: 并查集（Disjoint Set）是一种用于处理元素分组及查询两个元素是否属于同一组的数据结构。
top_img:
comments:
cover:
toc:
toc_number:
toc_style_simple:
copyright:
copyright_author:
copyright_author_href:
copyright_url:
copyright_info:
mathjax:
katex:
aplayer:
highlight_shrink:
aside:
abcjs:
---
# 并查集
并查集（Disjoint Set）是一种用于处理元素分组及查询两个元素是否属于同一组的数据结构。

``` C++
struct DSU {
    int n;
    std::vector<int> f, cntv;
    DSU(int size) : n(size), f(n), cntv(n, 1) {
        std::iota(f.begin(), f.end(), 0);
    }
    int find(int x) { 
        return f[x] == x ? x : f[x] = find(f[x]); 
    }
    bool same(int x, int y) { return find(x) == find(y); }
    bool merge(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) {
            return false;
        }
        cntv[x] += cntv[y];
        f[y] = x;
        return true;
    }
    int cnt_v(int x) { return cntv[find(x)]; }
};
```