---
title: Primes
date: 2023-03-10 16:18:12
updated: 2023-03-10 16:18:12
tags:
categories:
- [templates, math]
description: 线性筛，也称为埃拉托斯特尼筛法（Sieve of Eratosthenes），是一种用于求解素数的算法。
mathjax: true
---

# 线性筛
线性筛，也称为埃拉托斯特尼筛法（Sieve of Eratosthenes），是一种用于求解素数的算法。  
复杂度 $O(nlog^2{n})$

# Code

``` C++
constexpr int N = 1e7;
std::vector<int> primes;
int minp[N + 1]; // minp[i] = min prime factor of i
int num[N + 1]; // num[i] = number of prime factors of i
void init() {
    for (int i = 2; i <= N; i++) {
        if (!minp[i]) {
            minp[i] = i;
            primes.push_back(i);
            num[i] = 1;
        }
        for (auto p : primes) {
            if (i * p > N) break;
            minp[i * p] = p;
            num[i * p] = num[i] + 1;
            if (i % p == 0) break;
        }
    }
}
bool is_prime(int x) {
    if (x <= 1) {
        return false;
    }
    return minp[x] == x;
}
std::vector<int> get_facts(int x) {
    std::vector<int> facts;
    int t = x;
    while (t > 1) {
        if (facts.empty() || facts.back() != minp[t]) {
            facts.push_back(minp[t]);
        }
        t /= minp[t];
    }
    return facts;
}
```