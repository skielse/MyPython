import urllib2

__author__ = 'wangzijie'
print('aaaaabbbbbccccccccccc')
response = urllib2.urlopen("http://www.baidu.com")
print response.read()