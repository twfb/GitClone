# Git Clone

Git clone by downloading zip and decompressing it, the download speed is greatly improved.

## Installation
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
## How to use in Windows
1. `git-clone.bat`
```
@echo off  
python -c "exec('from git_clone import git_clone\nimport sys\ngit_clone(\'%1\')')"
```
2. add git-clone.bat in your Path
3. ![](images/windows.jpg)

## How to use in Linux
1. `git-clone.sh`
```
python -c "exec('from git_clone import git_clone\nimport sys\ngit_clone(\'$1\')')"
```
3. add git-clone.sh in your Path
4. ![](images/linux.jpg)
