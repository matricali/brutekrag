[![license](https://img.shields.io/github/license/jorge-matricali/brutekrag.svg)](https://jorge-matricali.mit-license.org/2014-2017) [![GitHub contributors](https://img.shields.io/github/contributors/jorge-matricali/brutekrag.svg)](https://github.com/jorge-matricali/brutekrag/graphs/contributors)
[![PyPI](https://img.shields.io/pypi/dm/brutekrag.svg)](https://pypi.python.org/pypi/brutekrag)

# brutekrag
Penetration tests on SSH servers using brute force or dictionary attacks. Written in _Python_.

> _brute krag_ means "brute force" in afrikáans

## Disclaimer
>This tool is for ethical testing purpose only.   
>brutekrag and its owners can't be held responsible for misuse by users.   
>Users have to act as permitted by local law rules.

## Requeriments
* Python 2.7
* see [requeriments.txt](requeriments.txt)

## Installation
It can be easily installed using _pip_

```bash
pip install brutekrag
```
Then you can do
```bash
$ brutekrag --help

usage: brutekrag [-h] [-t TARGET] [-T TARGETS] [-pF PASSWORDS] [-uF USERS]
                 [-sF SINGLE] [--separator SEPARATOR] [-p PORT] [-u USER]
                 [-P PASSWORD] [--timeout TIMEOUT]

      _                _       _
     | |              | |     | |
     | |__  _ __ _   _| |_ ___| | ___ __ __ _  __ _
     | '_ \| '__| | | | __/ _ \ |/ / '__/ _` |/ _` |
     | |_) | |  | |_| | ||  __/   <| | | (_| | (_| |
     |_.__/|_|   \__,_|\__\___|_|\_\_|  \__,_|\__, |
            OpenSSH Brute force tool 0.2.1     __/ |
          (c) Copyright 2014 Jorge Matricali  |___/


optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target hostname or IPv4.
  -T TARGETS, --targets TARGETS
                        Targets file that containas one hostname or IPv4 per line.
  -pF PASSWORDS, --passwords PASSWORDS
                        Path to password dictionary file. One password per line.
  -uF USERS, --users USERS
                        Path to users list file. One user per line.
  -sF SINGLE, --single SINGLE
                        Path to a file that contains a combination of both username and password. One combination per line, separated by space character by default.
  --separator SEPARATOR
                        Custom username/password separator. It's should be used in conjunction with -sF.
  -p PORT, --port PORT  Target port (default 22).
  -u USER, --user USER  Single user bruteforce.
  -P PASSWORD, --password PASSWORD
                        Single password bruteforce.
  --timeout TIMEOUT     Connection timeout (in seconds, 1 default).
```

## Example usages
```bash
# One target, one user, many passwords
brutekrag -t 10.10.0.14 --user root --passwords passwords.txt
# Many targets, one user, empty password
brutekrag -T targets.txt --user root --password ''
# One target, many pre-made combinations of user and password
brutekrag -t 192.168.0.1 --single combined.txt
```
