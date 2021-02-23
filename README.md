# Django-

如何利用git上传本地代码到github仓库

Quick setup — if you've done this kind of thing before

set up in Desktop or HTTPSssH https://github.com/yasina2020/Django-.git

Get started by creating a new file or uploading an existing file. We recommend every repository include a README,LCENSE, and .gitignore.

...or create a new repository on the command line

echo "# Django-” >>README .md

git init

git add README .md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/yasina2020/Django-.git

git push -u origin main


...or push an existing repository from the command line

git remote add origin https://github.com/yasina2020/Django-.git

git branch -M main

git push -u origin main


...or import code from another repository

You can initialize this repository with code from a Subversion,Mercurial, or TFS project.



2.23更新：自定义分页功能

```
from utils.MyPage import PageInfo
page_info = PageInfo(cur_page, 10, all_count, url='selfpage.html')
"""
:param cur_page: 当前页
:param per_page: 每页几条数据
:param all_count: 总行数
:param show_page: 显示多少个页码
:param url: 显示页码的网址
"""
```