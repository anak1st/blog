---
title: msys2
date: 2024-01-15 16:19:59
updated:
tags:
categories:
- [config]
description:
mathjax:
---

# Windows MSYS2 环境下 `ln -s`
默认情况下 msys2 会把 `ln -s` 变成复制动作  
如果启用原生软链接，`ln -s` 不能创建对不存在文件的链接

``` sh
ln -s /ucrt64/binmingw32-make.exe /ucrt64/bin/make.exe
```