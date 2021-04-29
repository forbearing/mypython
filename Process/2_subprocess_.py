#!/usr/bin/env python3

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit Code: ', r)

import subprocess 
print('$ nslookup')
p = subprocess.Popen(['nslookup'], 
        stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code: ', p.returncode)



===
1:subprocess
    1:可以用 os.system() 处理一些系统管理任务，运行 Linux 命令最简单的方式
    2:python 官方文档，应该用 subprocess 模块来运行系统命令，subprocess 模块允许我们
      创建子进程，连接他们的输入/输出/错误管道，并且获得返回值
    3:subprocess 模块打算用来替代几个过时的模块和函数，比如 os.system, os.spawn,
      os.popen, popen2
2:subprocess 模块
    subprocess.Popen
        创建并返回一个子进程，并在这个进程中执行指定的程序
    subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
        功能: 父进程直接创建子进程执行程序，然后等待子进程完成
        返回值: call() 返回子进程的 退出状态 即 child.returncode 属性
    subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
        功能: 父进程直接创建子进程执行程序，然后等待子进程完成
        返回值: 无论子进程是否成功，该函数都返回 0
            如果子进程的退出状态不是0，check_all() 抛出异常 CalledProcessError,
            异常对象中包含了 child.returncode 对应的返回码
    subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
        功能: 父进程直接创建子进程执行程序，以字符串的形式返回子进程的输出
        返回值: 字符串形式的子进程的输出结果, 推出状态不是0，抛出 CalledProcessError

3:其他
    Input and Output
        1:subprocess模块能阻止输出,当你不关心标准输出的时候是非常方便的
        2:它也使你通过一种正确的方式管理输入/输出,有条理地整合python脚本中的的shell命令
        3:我在使用subprocess时,有一个微妙的部分是怎么使用管道把命令连接起来，
          管道表明一个新的子管道应该被创建
          标准错误可以指向标准输出,表明子进程的错误信息会被捕获到和标准输出同一个文件
    Return Codes
        1:通过subprocess.call的返回值你能够判定命令是否执行成功
        2:每一个进程退出时都会返回一个状态码，你可以根据这个状态码写一些代码
        
        None    子进程尚未结束
        ==0     子进程正常退出
        >0      子进程异常退出，返回状态码
        <0      子进程被信号杀掉了



===
1:subprocess.call
    1:执行由参数提供的命令
    2:可以用数组作为参数运行命令,也可以用字符串作为参数运行命令(通过设置参数shell=True)
    3:注意,虽然你可以使用 "shell=True",但并不推荐这样的方式
    
    subprocess.call(['df', '-h'])
    subprocess.call("du -sh $HOME", shell=True)




===
1:subprocess.Popen()
    subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None,
    preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False,
    startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
    *, encoding=None, errors=None)

    1:subprocess模块中基本的进程创建和管理由Popen类来处理
    2:subprocess.popen是用来替代os.popen的

2:常用参数
    args:       shell命令，可以是字符串或者序列类型（如:list，元组)
    bufsize:
        缓冲区大小。当创建标准流的管道对象时使用，默认-1
        0:      不使用缓冲区
        1:      表示行缓冲，仅当universal_newlines=True时可用，也就是文本模式 
        正数：  表示缓冲区大小
        负数：  表示使用系统默认的缓冲区大小
    preexec_fn
        只在 Unix 平台下有效，用于指定一个可执行对象（callable object）
        它将在子进程运行之前被调用
    shell       如果该参数为 True，将通过操作系统的 shell 执行指定的命令
    cwd         用于设置子进程的当前目录
    env         用于指定子进程的环境变量。如果 env = None，子进程的环境变量将从父进程中继承
    

3:Popen 对象方法
    p.poll()        检查子进程  p 是否已经终止，返回 p.return code 属性
    p.send_signal(signal)       向子进程发送信号 signal
    p.terminate()               终止子进程p, 等于向子进程发送 SIGTERM 信号
    p.kill()                    杀死子进程 p ，等于向子进程发送 SIGKILL 信号
    p.wait()
        等待子进程 p 终止，返回 p.return code 属性
        wait() 立即阻塞父进程，直到子进程结束！
    p.communicate(input=None)
        和子进程进行交流，将参数 input（字符串）中的数据发送到子进程的 stdin，
        同时从子进程的 stdout 和 stderr 读取数据，直到 EOF
    
    import subprocess
    p = subprocess.Popen(["echo", "hello python"], stdout=subprocess.PIPE)
    print(p.communicate())

    from subprocess import Popen, PIPE
    p = Popen(["echo", "hello python.subprocess"], stdout=PIPE)
    print(p.communicate())
    stdout = p.communicate()[0].decode("utf8")
    print(stdout)

4:Popen.communicate()
    1:communicate()函数返回一个tuple(标准输出和错误)
    2:Popen.communicate()和进程沟通:发送数据到标准输入.从标准输出和错误读取数据
      直到遇到结束符.等待进程结束
    3:输入参数应该是一个字符串,以传递给子进程,如果没有数据的话应该是None
    4:基本上,当你用communicate()函数的时候意味着你要执行命令了
    5:返回值: 二元组 (stdoutdata, stderrdata) 分别表示从标准出和标准错误中读出的数据
    6:只能通过管道和子进程通信，也就是说，只有调用 Popen() 创建子进程的时候参数 
     stdin=subprocess.PIPE，才能通过 p.communicate(input) 向子进程的 stdin 发送数据；
     只有参数 stout 和 stderr 也都为 subprocess.PIPE ，才能通过p.communicate() 从
     子进程接收数据，否则接收到的二元组中，对应的位置是None。
    

