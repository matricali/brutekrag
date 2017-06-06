"""
MIT License

Copyright (c) 2014-2017 Jorge Matricali

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
from __future__ import print_function
import sys
import paramiko
from paramiko import AutoAddPolicy
import socket


class brutekrag:
    def __init__(self, host, port=22, timeout=1):
        self.host = host
        self.port = port
        self.list_users = []
        self.list_passwords = []
        self.timeout = timeout

    def connect(self, username, password):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(
                self.host,
                port=self.port,
                username=username,
                password=password,
                timeout=self.timeout
            )

        except paramiko.AuthenticationException:
            return False

        except (paramiko.ssh_exception.BadHostKeyException) as error:
            raise Exception('[%s:%d] BadHostKeyException: %s' % (self.host, self.port, error.message))
            return False

        except (paramiko.ssh_exception.SSHException, socket.error) as se:
            raise Exception('[%s:%d] Connection error: %s' % (self.host, self.port, str(se)))
            return False

        except paramiko.ssh_exception.SSHException as error:
            raise Exception('[%s:%d] An error occured: %s' % (self.host, self.port, error.message))
            return False

        finally:
            client.close()

        return True
