#!/usr/bin/env python3

# import subprocess

# subprocess.call(['df', '-h'])
# subprocess.call("du -sh $HOME/Downloads", shell=True)
# p = subprocess.Popen(["echo", "hello python"], stdout=subprocess.PIPE)
# print(p.communicate())

from subprocess import Popen, PIPE

p = Popen(["echo", "hello python.subprocess"], stdout=PIPE)
stdout = p.communicate()[0].decode("utf8")
print(stdout)
