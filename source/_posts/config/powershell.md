---
title: PowerShell Config
date: 2024-01-15 16:19:59
updated:
tags:
categories:
- [config]
description:
mathjax:
---

# PowerShell 配置

``` powershell
# Auto suggestions
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

# Oh My Posh
# $MY_POSH_THEMES_PATH = "E:\GitHub\Settings\powershell\xf.omp.json"
# oh-my-posh init pwsh --config $MY_POSH_THEMES_PATH | Invoke-Expression

# Starship
Invoke-Expression (&starship init powershell)

# Disable Python venv prompt prefix
# $Env:VIRTUAL_ENV_DISABLE_PROMPT = 1

# Set-Proxy
$Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890"

# $Env:ElECTRON_MIRROR="https://npmmirror.com/mirrors/electron/"

function Start-Conda {
    If (Test-Path "C:\Users\Anak1st\miniconda3\Scripts\conda.exe") {
        (& "C:\Users\Anak1st\miniconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | ?{$_} | Invoke-Expression
    }
}

function Add-Msys2Path {
    $msys2Path = "C:\msys2\usr\bin"
    $Env:Path += ";$msys2Path"
}
```