#! /usr/bin/python

import sys, time
import fileinput
import calendar
import collections
from urlparse import urlparse


user_dict = collections.OrderedDict()
maxlen = 10000000

def getTime(rawTime):
    return str(calendar.timegm(time.strptime(rawTime, "%Y-%m-%d %H:%M:%S")))


def normalizeUrl(url):
    o = urlparse(url)
    return "  " + o.netloc.replace("www.","") + o.path

def getUid(ip, user_agent, url):
    return ip + user_agent + url


def build(timestamp, host, uri, code, size):
    return "|".join([timestamp, host, uri, code, size])

def transform(raw):
    tokens = raw.split('\t')
    uid = getUid(tokens[6], tokens[7], tokens[13])

    line = None

    if tokens[12] == "AD_VIEW":
        if len(user_dict) >= maxlen:
            user_dict.popitem(last = False)
        user_dict[uid] = False
    elif tokens[12] == "AD_CLICK" or tokens[12] == "AD_TAP":
        if uid in user_dict:
            user_dict[uid] = True
    elif tokens[12] == "PAGE_EXIT":
        if uid in user_dict:
            status = user_dict.pop(uid)
            if status == True:
                line = build(getTime(tokens[0]), tokens[16], normalizeUrl(tokens[13]), "400", "50000")
            else:
                line = build(getTime(tokens[0]), tokens[16], normalizeUrl(tokens[13]), "200", "50000")
    return line


def main(argv):
    for rawLine in fileinput.input():
        line = transform(rawLine)
        if line != None:
            print line

if __name__ == '__main__':
    main(sys.argv)
