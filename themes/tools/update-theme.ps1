Remove-Item .\next -Recurse -Force
git clone "https://github.com/theme-next/hexo-theme-next" .\next
Remove-Item .\next\.git -Recurse -Force