#!/usr/bin/env python3

import os
import sys
import crypt
import getopt
import random
import string

def getsalt(chars=string.ascii_letters + string.digits):
    return random.choice(chars) + random.choice(chars)

def save(outfile, user, passwd):
    with open(outfile, "w") as f:
        f.write(user + ":" + crypt.crypt(passwd,salt))
        f.write('\n')


if __name__ == '__main__':
    output_file = user = passwd = None
    if len(sys.argv) > 1:
        try:
            opts, _ = getopt.getopt(sys.argv[1:], 'u:p:f:h')
        except getopt.GetoptError as e:
            print('error', e)
            sys.exit(2)

		for o, a in opts:
            if o in ('-f'):
                output_file = os.path.abspath(a)
            elif o in ('-u'):
                user = a
            elif o in ('-p'):
                password = a
            elif o in ('-h'):
                print("where options are\n-f filename\n-p password\n-u u
		exit() else:
		assert False, 'unhandled option'

