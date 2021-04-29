auth-v1.py
    import crypt
    import random,string

    def getsalt(chars=string.ascii_letters + string.digits):
        return random.choice(chars) + random.choice(chars)

    salt = getsalt()
    print(crypt.crypt('hybfkuf', salt))


auth-v2
    import crypt
    import sys
    import random,string

    if len(sys.argv) != 4:
        print("Usage: {0} [user|password|file_name]".format(sys.argv[0]))
        sys.exit(1)
    user = sys.argv[1]
    passwd = sys.argv[2]
    file_name = sys.argv[3]

    def getsalt(chars=string.ascii_letters + string.digits):
        return random.choice(chars) + random.choice(chars)

    with open(file_name, 'w') as f:
        salt = getsalt()
        print('success!')
        f.write(user+":"+crypt.crypt(passwd,salt))
        f.write('\n')


auth-v3
    import crypt
    import sys
    import random,string
    from optparse import OptionParser

    def getsalt(chars=string.ascii_letters + string.digits):
        return random.choice(chars) + random.choice(chars)

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="write report to file", metavar="FILE")
    parser.add_option("-u", "--user", dest="user", type="string", help="it is user")
    parser.add_option("-p", "--passwd", dest="passwd", help="it is password")
    (options, args) = parser.parse_args()

    with open(options.filename, "w") as f:
        salt = getsalt()
        print("success")
        f.write(options.user+":"+crypt.crypt(options.passwd,salt))
        f.write("\n")


auth-v4 (这个版本的笔记没做)
