---
title: String Hash
date: 2023-03-10 16:18:12
updated: 2023-03-10 16:18:12
tags:
categories:
- [templates, string]
description: 双模哈希（Double Hashing）是一种解决哈希冲突的方法，它通过使用两个哈希函数来确定冲突时的下一个可用位置。
---

# 双模哈希
双模哈希（Double Hashing）是一种解决哈希冲突的方法，它通过使用两个哈希函数来确定冲突时的下一个可用位置。

# #includes
- [templates/Math/Number/Mint.hpp](/blog/templates/math/mint/)

# Code

``` C++
#include "templates/Math/Number/Mint.hpp"

constexpr i64 Mod1 = 1e9 + 7, Mod2 = 1e9 + 9;
struct Hash {
    MintBase<Mod1> m1;
    MintBase<Mod2> m2;
    Hash() : m1(0), m2(0) {}
    Hash(i64 x, i64 y) : m1(x), m2(y) {}
    Hash(MintBase<Mod1> x, MintBase<Mod2> y) : m1(x), m2(y) {}
    std::pair<i64, i64> val() const {
        return {m1.val(), m2.val()};
    }
    friend Hash operator+(const Hash &lhs, const Hash &rhs) {
        return Hash(lhs.m1 + rhs.m1, lhs.m2 + rhs.m2);
    }
    friend Hash operator-(const Hash &lhs, const Hash &rhs) {
        return Hash(lhs.m1 - rhs.m1, lhs.m2 - rhs.m2);
    }
    friend Hash operator*(const Hash &lhs, const Hash &rhs) {
        return Hash(lhs.m1 * rhs.m1, lhs.m2 * rhs.m2);
    }
    friend bool operator==(const Hash &lhs, const Hash &rhs) {
        return lhs.m1 == rhs.m1 && lhs.m2 == rhs.m2;
    }
} Base(13331, 23333);

std::vector<Hash> PW{Hash(1, 1)};
void init(int n) {
    if (n + 1 <= (int)PW.size()) {
        return;
    }
    int m = (int)PW.size() - 1;
    PW.resize(n + 1);
    for (int i = m + 1; i <= n; ++i) {
        PW[i] = PW[i - 1] * Base;
    }
}
std::vector<Hash> get(std::string s) {
    int n = (int)s.size();
    std::vector<Hash> res(n + 1);
    for (int i = 0; i < n; ++i) {
        res[i + 1] = res[i] * Base + Hash(s[i], s[i]);
    }
    return res;
}
void example() {
    std::string s;
    auto h = get(s);
    auto sub = [&](int l, int r) -> Hash {
        return h[r] - h[l] * PW[r - l];
    };
}
```