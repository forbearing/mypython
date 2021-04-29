---
# Popen 类处理进程的创建和管理. 通过使用这一模块, 开发人员可以处理不太常见的用例.
# 子进程将在新的进程中进行. 要在Unix/Linux上执行子程序，该类会使用os.execvp()函数. 
# 要在Windows上执行子程序, 该类会使用CreateProcess()函数
import subprocess, sys

HOST = "hybfkuf@192.168.20.200"
COMMAND = "ls"

ssh_obj =subprocess.Popen(["ssh", "%s" %HOST, COMMAND],
        shell = False,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)
result = ssh_obj.stdout.readlines()
if result ==  []:
    err = ssh_obj.stderr.readlines()
    print(sys.stderr, "ERROR: %s" %err)
else:
    print(result)
