文件的打开和关闭
    1:使用 open 函数，可以打开一个已经存在的文件，后者创建一个新文件
    2:open(文件名，访问模式)
        f = open('test.txt','w')
        f.write('hello python')
        f.close()
    3:访问模式
        r       只读模式打开文件，文件的指针将会放在文件的开头。这是默认模式
        w       打开一个只用于写入，如果该文件存在则将其覆盖，不存在则创建文件
        a       打开一个文件用户追加，如果文件已存在，文件指针将会放在文件的末尾，也就是说，新的
                内容将会被写入到已有的内容之后。如果该文件不存在，创建新文件进行写入。
        rb      以二进制格式打开一个文件，只文指针会放在文件的开头，这是默认模式
        wb      以二进制格式打开一个文件只用于写入，如果该文件存在则覆盖，如果不存在则创建新文件
        ab      以二进制格式打开一个文件用户追加，如果该文件已存在，文件指针会放在文件的末尾，
                也就是说，新的内容将会被写入到已有内容之后，如果该文件不存在，创建新文件进行写入
        r+      打开一个文件用于读写，文件指针将会放在开头
        w+      打开一个文件用于读写，文件存在覆盖，不存在创建新文件
        a+      打开一个文件用于读写，文件存在，将文件指针放在文件的结尾，不存在创建
        rb+     wb+     ab+


文件的读写
    1:写数据
        1:使用 write() 可以完成向文件写入数据
        2:使用
            f = open('test.txt','w')
            f.write("i'm not a robot")
            f.close()
    2:读数据
        1:使用 read(num) 可以从文件中读取数据，num 表示要从文件中读取的数据的长度（单位是字节），
          如果没有传入 num，那么就表示读取文件中的所有数据
        2:使用
            f = open('test.txt','r')
            content = f.read(5)
            print(content)
            print('-'*30)
        3:readlines
            就像 read 没有参数一样，readlines 可以按照行的方式把整个文件中的内容进行一次性读取，
            并且返回的是一个列表，其中每一行的数据为一个元素
            f = open('test.txt','r')
            conetnt f.readlines()
            print(type(content))
            i = 1
            for temp in content:
                print ("%d:%s"%(i, temp))
                i += 1
            f.close()
        4:readline
            f = open('test.txt','r')
            content = f.readline()
            print("1:%s"%content)
            content = f.readline()
            print("2:%s"%content)
            f.close()


文件的拷贝
    1:使用
        src_file = '/etc/services'
        dest_file = src_file[src_file.rfind('/')+1:]+".copy"
        print("目标文件名为: %s"%dest_file)
        # 打开文件
        src_f = open(src_file,'rb')
        dest_f = open(dest_file,'wb')
        # 读写文件
        content = src_f.read()
        dest_f.write(content)
        # 关闭文件
        src_f.close()
        dest_f.close()


文件的定位
    1:获取当前读写的位置: tell()
        f = open('test.txt','r')
        str = f.read(3)
        pos = f.tell()
        print("文件的位置: %s"%pos)
        f.close()
    2:定位到某个位置
        1:如果在读写文件的过程中，需要从另一个位置进行操作的话，可以使用 seek()
        2:seek(offset, from) 
            offset      偏移量
            from        方向
                0，表示开头
                1，表示当前位置
                2，表示文件末尾
        3:示例：把位置设置为：从文件开头，偏移5个字节
            f = open('test.txt','r')
            str = f.read(30)
            pos = f.tell()
            print("当前文件的位置是：%s"%pos)
            f.seek(5,0)
            pos = f.tell()
            print("现在的位置是：%s",%pos)


os 模块
    - 有些时候，需要对文件进行重命名、删除等一些操作，python os 模块有这个功能
    - python 编程时，经常和文件和目录打交道，这就离不开 os 模块，os 模块包含普遍的操作系统功能，
      与具体的平台无关
    1:常用的 os 模块的方法
        import os
        os.name()           判断当前正在使用的平台，windows 返回 nt，linux 返回 posix
        os.getcwd()         返回当前工作目录
        os.listdir()        指定所有目录下所有的文件和目录名
        os.remove()         删除指定文件和目录名
        os.rmdir()          删除指定目录
        os.mkdir()          创建目录
        os.rename()         重命名
        os.makedirs()       创建多级目录
        os.path.isfile()    判断对象是否为文件，True/False
        os.path.isdir()     判断对象是否为目录，True/False
        os.path.exists()    检验指定的对象是否存在，True/False
        os.path.split()     返回路径的目录和文件名
        os.system()         执行 shell 命令
        os.chdir()          改变工作目录
        os.path.getsize()   获取文件大小
        os.path.abspath()   获取绝对路径
        os.path.join(path,name)     连接目录和文件名
        os.path.basename(path)      返回文件名
        os.path.dirname(path)       返回文件所目录 
    3:应用：批量修改文件名
        import os
        file_list = os.listdir('test/')
        for item in file_list:
            dest_file = f + ".new"
            parent_dir = os.path.abspath("test")
            src_file = os.path.join(parent_dir,f)
            dest_file = os.path.join(parent_dir,dest_file)
            os.rename(src_file,dest_file)

        import os
        file_list = os.listdir('test/')
        for f in file_list:
            src_file = os.path.abspath(f)
            dest_file = os.path.abspath(f) + ".new"
            os.rename(src_file, dest_file)




=== 2020-4

    ---
    with open('/tmp/file.txt', 'r', encoding='gbk', errors='ignore')  as myfile:
        data = myfile.read()
        print(data)
        # 当文件编码是 'utf-8' 格式时，却打开格式为gbk格式时，会报错，
        # 如果加上 errors='ignore' 这不会报错
    with open('/tmp/file.txt', 'rb') as myfile:
        data = myfile.read()
        newdata = data.decode('utf-8')
        print(newdata)
        # rb 模式没有 encoding 和 errors 参数
        # rb 模式下的 data 才有 data.deocde() 方法

    --- pickle 持久化
    import pickle

    list1 = [1,2,3,4, "hello python"]
    path = "/tmp/file.txt"

    with open(path, 'wb') as myfile:
        pickle.dump(list1, myfile)

    with open(path, 'rb') as myfile:
        data = pickle.load(myfile)
        print(data)

    --- StringIO
    1:StringIO 是在内存中读写 str
    from io import StringIO
    f = StringIO()
    f.write('hello')

    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())
    f.write('python')
    print(f.getvalue())

    --- BytesIo
    1:StringIO 操作的只能是 Str，如果要操作二进制数据，就需要使用 BytesIO
    2:BytesIO 实现了在内存中读取 bytes
    from io import BytesIO
    f = BytesIO()
    f.write('􏳼􏴢'.encode('utf-8'))
    print(f.getvalue)

    from io import BytesIO
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    f.read()

with
    1:并不是所有的 open() 函数返回的 fp 对象才能使用 with 语句。实际上，任何对象，
      只要正确实现了上下文管理，都可以用于 with 语句
    2:实现了上下文管理是通过 __enter__ 和 __exit__ 两个方法来实现的。
    ---
    class Query(object):
        def __init__(self, name):
            self.name = name
        def __enter__(self):
            print('Begin')
            return self
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type:
                print('Error')
            else:
                print('End')
        def query(self):
            print("Query info about %s ..." %self.name)
    with open('hybfkuf') as q:
        q.query()
