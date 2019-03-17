# git-clone

Git clone by downloading zip and decompressing it, the download speed is greatly improved.

## Installation
python2 need 2.7.9+
```
$ pip install git-clone
```

## How to use in py file
```
from git_clone import git_clone
git_clone('https://github.com/dhgdhg/git-clone.git')
git_clone('https://github.com/dhgdhg/git-clone/', 'E:/')
git_clone('https://github.com/dhgdhg/git-clone', 'E:/', 'master')
```
## How to use in command
```
git-clone https://github.com/dhgdhg/git-clone.git
git-clone https://github.com/dhgdhg/git-clone.git E:/
git-clone https://github.com/dhgdhg/git-clone.git E:/ master
```