#!/usr/bin/env python3

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write report to file", metavar="FILE")
parser.add_option("-u", "--user", dest="user", type="string", help="it is user")
parser.add_option("-p", "--passwd", dest="passwd", help="it is password")

(options, args) = parser.parse_args()
print(options.filename)
print(options.passwd)
print(options.user)
